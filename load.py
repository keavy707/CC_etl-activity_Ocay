import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine

def load_presentation(df_final):
   """
   This creates the final consolidated “BIG TABLE”.
   Loads all cleaned Japan + Myanmar tables from the transformation DB.
   Creates the final consolidated table in Render PostgreSQL.
   """
   DATABASE_URL = "postgresql://cc_db_act_user:lEL8rkE2QfX4WnDrAQvfvyRPZn9blMVw@dpg-d7u3e1tckfvc73ej116g-a.singapore-postgres.render.com/cc_db_act"
    
   # Create the SQLAlchemy engine
   engine = create_engine(DATABASE_URL)

   # Upload to Render (Table name: presentation_consolidated)
   df_final.to_sql('presentation_consolidated', con=engine, if_exists='replace', index=False)
    
   print("Load successful: Data is now available in your Render Database.")
