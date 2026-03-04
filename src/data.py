"""Shared data loading and cleaning utilities for the Online Retail dataset."""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def load_raw() -> pd.DataFrame:
    """Load the raw Online Retail Excel file and return as a DataFrame."""
    return pd.read_excel(RAW_DATA_PATH, dtype={"CustomerID": str})


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply standard cleaning steps to the raw Online Retail DataFrame.

    Steps:
    1. Drop rows with missing CustomerID
    2. Remove cancelled invoices (InvoiceNo starting with 'C')
    3. Remove rows where Quantity <= 0 or UnitPrice <= 0
    4. Strip whitespace from Description
    5. Add derived column TotalPrice = Quantity * UnitPrice
    """
    df = df.copy()

    # 1. Drop missing CustomerID
    df = df.dropna(subset=["CustomerID"])

    # 2. Remove cancellations
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    # 3. Remove non-positive quantities and prices
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # 4. Strip whitespace from Description
    df["Description"] = df["Description"].astype(str).str.strip()

    # 5. Add TotalPrice
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df.reset_index(drop=True)
