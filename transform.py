import sqlite3
import pandas as pd

def clean_sqlite_table():

    """
    read from staging and perform data cleaning
    Standardize values across datasets (e.g., Japan store item prices in JPY and Myanmar store item prices in USD are converted to a common currency or format).
    """
    # Connect to SQLite
    # Read table into DataFrame
    # ------------------------------
    # EXAMPLE DATA CLEANING STEPS
    # ------------------------------
    # 1. Strip extra whitespace from column names
    # 2. Strip whitespace inside text columns
    # 3. Replace empty strings with NaN
    # 4. Drop duplicate rows
    # ------------------------------
    # SAVE CLEANED DATA
    # ------------------------------

