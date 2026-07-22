"""
01_inspect_data.py

Initial inspection of the ASAP 2.0 essay-scoring dataset.

Purpose
-------
This script:
1. Lists raw dataset files.
2. Identifies CSV files.
3. Loads candidate datasets.
4. Reports dimensions, variables, missingness, and score distributions.
5. Does not modify the original data.

Author: Dr. Itauma Itauma
Project: LLM Prompt-Induced Measurement Variability
"""

from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def list_raw_files() -> list[Path]:
    """Return all files contained in the raw-data directory."""
    return sorted(
        file
        for file in RAW_DATA_DIR.rglob("*")
        if file.is_file() and file.name != ".gitkeep"
    )


def inspect_csv(file_path: Path) -> None:
    """Print a structured inspection of a CSV file."""

    print("\n" + "=" * 80)
    print(f"FILE: {file_path.name}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)
    except Exception as exc:
        print(f"Could not read file: {exc}")
        return

    print(f"\nRows:    {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    print("\nCOLUMN NAMES")
    print("-" * 80)

    for column in df.columns:
        print(column)

    print("\nDATA TYPES")
    print("-" * 80)
    print(df.dtypes)

    print("\nMISSING VALUES")
    print("-" * 80)

    missing = (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )

    print(missing[missing > 0])

    print("\nFIRST FIVE ROWS")
    print("-" * 80)

    # Do not print full essay text because it can overwhelm the console.
    preview = df.head().copy()

    for column in preview.columns:
        if preview[column].dtype == "object":
            preview[column] = (
                preview[column]
                .astype(str)
                .str.replace("\n", " ", regex=False)
                .str.slice(0, 120)
            )

    print(preview.to_string(index=False))

    # Look for likely scoring variables.
    score_columns = [
        column
        for column in df.columns
        if any(
            term in column.lower()
            for term in ["score", "rating", "grade"]
        )
    ]

    if score_columns:
        print("\nPOTENTIAL SCORE VARIABLES")
        print("-" * 80)

        for column in score_columns:
            print(f"\n{column}")
            print(df[column].describe())
            print("\nValue counts:")
            print(
                df[column]
                .value_counts(dropna=False)
                .sort_index()
                .head(30)
            )


def main() -> None:
    """Run raw-data inspection."""

    print("\nASAP 2.0 RAW DATA INSPECTION")
    print("=" * 80)

    files = list_raw_files()

    if not files:
        raise FileNotFoundError(
            f"No files found in {RAW_DATA_DIR}. "
            "Download and extract ASAP 2.0 before running this script."
        )

    print("\nRAW FILES FOUND")
    print("-" * 80)

    for file in files:
        relative_path = file.relative_to(PROJECT_ROOT)
        size_mb = file.stat().st_size / (1024 ** 2)

        print(f"{relative_path} ({size_mb:.2f} MB)")

    csv_files = [
        file
        for file in files
        if file.suffix.lower() == ".csv"
    ]

    print(f"\nCSV files found: {len(csv_files)}")

    for file in csv_files:
        inspect_csv(file)


if __name__ == "__main__":
    main()