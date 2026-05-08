import sqlite3
import pandas as pd

def clean_data(j_branch, j_customers, j_items, j_payment,
               m_branch, m_customers, m_items, m_payment, sales):

    """
    read from staging and perform data cleaning
    Standardize values across datasets (e.g., Japan store item prices in JPY and Myanmar store item prices in USD are converted to a common currency or format).
    """
    # Connect to SQLite
    # Read table into DataFrame

    # 1. Standardize Headers
    for df in [j_branch, j_customers, j_items, j_payment, 
               m_branch, m_customers, m_items, m_payment, sales]:
        df.columns = df.columns.str.strip().str.replace("'", "").str.lower().str.replace(" ", "_")

    # 2. Rename columns to match across countries
    j_items = j_items.rename(columns={'product_name': 'item_name', 'category': 'item_category'})
    m_items = m_items.rename(columns={'name': 'item_name', 'type': 'item_category'})
    j_customers = j_customers.rename(columns={'membership': 'customer_type'})
    m_customers = m_customers.rename(columns={'type': 'customer_type'})
    j_payment = j_payment.rename(columns={'name': 'payment_method'})
    m_payment = m_payment.rename(columns={'name': 'payment_method'})

    # 3. Currency Conversion (Standardizing to USD)
    # Japan: ~155 JPY to 1 USD | Myanmar: ~2100 MMK to 1 USD
    j_items['price_usd'] = j_items['price'] / 155
    m_items['price_usd'] = m_items['price'] / 2100

    # 4. Add Location Tags (The "Composite Key" prep)
    for df in [j_branch, j_customers, j_items, j_payment]:
        df['store_location'] = 'Japan'
    for df in [m_branch, m_customers, m_items, m_payment]:
        df['store_location'] = 'Myanmar'

    # 5. Assigning sales to locations
    # Since sales_data.csv only has IDs 1, 2, 3, we split it 50/50
    sales['store_location'] = 'Japan'
    sales.loc[sales.index % 2 == 1, 'store_location'] = 'Myanmar'

    # 6. Combine Lookups
    all_items     = pd.concat([j_items,     m_items],     ignore_index=True)
    all_branches  = pd.concat([j_branch,    m_branch],    ignore_index=True)
    all_customers = pd.concat([j_customers, m_customers], ignore_index=True)
    all_payments  = pd.concat([j_payment,   m_payment],   ignore_index=True)

    # 7. Build the Big Table using Composite Keys (ID + Location)
    # This ensures 'Japan Branch 1' doesn't match 'Myanmar Branch 1'
    df_final = sales.merge(all_items, 
                           left_on=['product_id', 'store_location'], 
                           right_on=['id', 'store_location'], how='inner')
    
    df_final = df_final.merge(all_branches, 
                              left_on=['branch_id', 'store_location'], 
                              right_on=['id', 'store_location'], 
                              how='inner', suffixes=('', '_branch'))
    
    df_final = df_final.merge(all_customers, 
                              left_on=['customer_id', 'store_location'], 
                              right_on=['id', 'store_location'], 
                              how='inner', suffixes=('', '_customer'))
    
    df_final = df_final.merge(all_payments, 
                              left_on=['payment', 'store_location'], 
                              right_on=['id', 'store_location'], 
                              how='inner', suffixes=('', '_payment'))

    # 8. Cleanup extra columns
    cols_to_drop = ['id', 'id_branch', 'id_customer', 'id_payment', 'payment', 'price']
    df_final.drop(columns=[c for c in cols_to_drop if c in df_final.columns], inplace=True)

    print(f"Successfully compiled {len(df_final)} rows.")
    print(f"Location distribution:\n{df_final['store_location'].value_counts()}")
    
    return df_final