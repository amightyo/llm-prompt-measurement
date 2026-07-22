"""
02_prepare_sample.py

Create a reproducible stratified sample from the ASAP 2.0 dataset.

Design
------
Task: Facial action coding system
Human reference scores: 1-6
Sample: 30 essays per score level
Total analytic sample: 180 essays

The sampling procedure uses a fixed random seed for reproducibility.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ASAP2_train_sourcetexts.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "analytic_sample.csv"
)

TARGET_PROMPT = "Facial action coding system"

N_PER_SCORE = 30

RANDOM_SEED = 20260722


def main():

    print("\n" + "=" * 80)
    print("CREATING ANALYTIC SAMPLE")
    print("=" * 80)

    # ---------------------------------------------------------------
    # Load data
    # ---------------------------------------------------------------

    df = pd.read_csv(RAW_FILE)

    print(f"\nFull dataset: {len(df):,} essays")

    # ---------------------------------------------------------------
    # Restrict to selected educational task
    # ---------------------------------------------------------------

    task_df = df.loc[
        df["prompt_name"] == TARGET_PROMPT
    ].copy()

    print(
        f"Selected task: {TARGET_PROMPT}"
    )

    print(
        f"Task population: {len(task_df):,} essays"
    )

    # ---------------------------------------------------------------
    # Verify score distribution
    # ---------------------------------------------------------------

    print("\nPopulation score distribution:")

    print(
        task_df["score"]
        .value_counts()
        .sort_index()
    )

    # ---------------------------------------------------------------
    # Verify sufficient essays
    # ---------------------------------------------------------------

    score_counts = task_df["score"].value_counts()

    for score in range(1, 7):

        available = score_counts.get(score, 0)

        if available < N_PER_SCORE:
            raise ValueError(
                f"Score {score} contains only {available} essays. "
                f"At least {N_PER_SCORE} are required."
            )

    # ---------------------------------------------------------------
    # Stratified random sample
    # ---------------------------------------------------------------

    sampled_groups = []

    for score in range(1, 7):

        score_group = task_df.loc[
            task_df["score"] == score
        ]

        sample = score_group.sample(
            n=N_PER_SCORE,
            random_state=RANDOM_SEED + score
        )

        sampled_groups.append(sample)

    analytic_sample = pd.concat(
        sampled_groups,
        ignore_index=True
    )

    # ---------------------------------------------------------------
    # Shuffle final dataset
    # ---------------------------------------------------------------

    analytic_sample = (
        analytic_sample
        .sample(
            frac=1,
            random_state=RANDOM_SEED
        )
        .reset_index(drop=True)
    )

    # ---------------------------------------------------------------
    # Add anonymous analytic ID
    # ---------------------------------------------------------------

    analytic_sample.insert(
        0,
        "analytic_id",
        [
            f"E{i:03d}"
            for i in range(
                1,
                len(analytic_sample) + 1
            )
        ]
    )

    # ---------------------------------------------------------------
    # Retain only variables needed for primary analysis
    # ---------------------------------------------------------------

    analytic_sample = analytic_sample[
        [
            "analytic_id",
            "essay_id",
            "score",
            "full_text",
            "assignment",
            "prompt_name",
            "source_text_1",
            "source_text_2",
            "source_text_3",
            "source_text_4",
        ]
    ]

    # ---------------------------------------------------------------
    # Save
    # ---------------------------------------------------------------

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    analytic_sample.to_csv(
        OUTPUT_FILE,
        index=False
    )

    # ---------------------------------------------------------------
    # Verification
    # ---------------------------------------------------------------

    print("\n" + "=" * 80)
    print("ANALYTIC SAMPLE CREATED")
    print("=" * 80)

    print(
        f"\nTotal sampled essays: "
        f"{len(analytic_sample):,}"
    )

    print("\nSample score distribution:")

    print(
        analytic_sample["score"]
        .value_counts()
        .sort_index()
    )

    print(
        f"\nOutput saved to:\n{OUTPUT_FILE}"
    )

    print("\nFirst 10 analytic IDs:")

    print(
        analytic_sample[
            ["analytic_id", "score"]
        ]
        .head(10)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()