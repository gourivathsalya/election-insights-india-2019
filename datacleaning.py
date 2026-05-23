
import pandas as pd
import numpy as np

def load_and_clean():
    print("=" * 50)
    print("  STEP 1: LOADING & CLEANING DATA")
    print("=" * 50)

    # Load raw data
    df = pd.read_csv('data/electionanalysis.csv')
    print(f"\n Raw data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # Fix column names (remove newlines and extra spaces)
    df.columns = df.columns.str.replace('\n', ' ').str.strip()
    print(" Column names cleaned")

    # Show missing values before cleaning
    print("\n── Missing Values (Before Cleaning) ──")
    missing = df.isnull().sum()
    print(missing[missing > 0])

    # Drop rows with missing values
    df_clean = df.dropna().copy()
    print(f"\n Dropped missing rows: {len(df) - len(df_clean)} rows removed")
    print(f" Clean dataset: {df_clean.shape[0]} rows remaining")

    # Clean ASSETS column (remove Rs, commas, spaces)
    df_clean['ASSETS'] = (
        df_clean['ASSETS']
        .str.replace('Rs ', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    df_clean['ASSETS'] = pd.to_numeric(df_clean['ASSETS'], errors='coerce')

    # Clean LIABILITIES column
    df_clean['LIABILITIES'] = (
        df_clean['LIABILITIES']
        .str.replace('Rs ', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    df_clean['LIABILITIES'] = pd.to_numeric(df_clean['LIABILITIES'], errors='coerce')

    # Clean CRIMINAL CASES column
    df_clean['CRIMINAL CASES'] = pd.to_numeric(df_clean['CRIMINAL CASES'], errors='coerce')

    print(" ASSETS, LIABILITIES, CRIMINAL CASES columns converted to numeric")

    # Save cleaned data
    df_clean.to_csv('data/cleaned_election_data.csv', index=False)
    print("\n Cleaned data saved to: data/cleaned_election_data.csv")

    # Summary
    print("\n── Dataset Summary ──")
    print(f"Total candidates : {len(df)}")
    print(f"Clean records    : {len(df_clean)}")
    print(f"Total states     : {df_clean['STATE'].nunique()}")
    print(f"Total parties    : {df_clean['PARTY'].nunique()}")
    print(f"Total winners    : {df_clean['WINNER'].sum()}")
    print(f"Average age      : {round(df_clean['AGE'].mean(), 1)} years")

    print("\n Data cleaning complete!")
    return df_clean

if __name__ == '__main__':
    load_and_clean()