import pandas as pd
import os

def load_csv():
    """
    write a script that loads source csv data to sqlite file in the staging area 
    """
    # conn = sqlite3.connect(sqlite_path)
    # df = pd.read_csv(csv_path)
    # df.to_sql(table_name, conn, if_exists='replace', index=False)

    """
    Extracts all CSV files from the local folders.
    """
    # Define folder names
    japan_dir = 'japan_store'
    myanmar_dir = 'myanmar_store'

    # Load all 4 Japan files
    j_branch = pd.read_csv(os.path.join(japan_dir, 'japan_branch.csv'))
    j_cust = pd.read_csv(os.path.join(japan_dir, 'japan_Customers.csv'))
    j_items = pd.read_csv(os.path.join(japan_dir, 'japan_items.csv'))
    j_pay = pd.read_csv(os.path.join(japan_dir, 'japan_payment.csv'))

    # Load all 4 Myanmar files
    m_branch = pd.read_csv(os.path.join(myanmar_dir, 'myanmar_branch.csv'))
    m_cust = pd.read_csv(os.path.join(myanmar_dir, 'myanmar_customers.csv'))
    m_items = pd.read_csv(os.path.join(myanmar_dir, 'myanmar_items.csv'))
    m_pay = pd.read_csv(os.path.join(myanmar_dir, 'myanmar_payment.csv'))

    # Load shared sales data from root
    sales = pd.read_csv('sales_data.csv')

    print("Extraction successful: All 9 source files loaded.")
    return j_branch, j_cust, j_items, j_pay, m_branch, m_cust, m_items, m_pay, sales