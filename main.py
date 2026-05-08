import extract
import transform
import load

# 1. Extract
(j_branch, j_customers, j_items, j_payment,
 m_branch, m_customers, m_items, m_payment, sales) = extract.load_csv()

# 2. Transform
cleaned_data = transform.clean_data(
    j_branch, j_customers, j_items, j_payment,
    m_branch, m_customers, m_items, m_payment, sales
)
# 3. Load
load.load_presentation(cleaned_data)

print("\n--- ETL Activity Complete ---")
print("Check pgAdmin and refresh your 'Tables' to see 'presentation_consolidated'.")
