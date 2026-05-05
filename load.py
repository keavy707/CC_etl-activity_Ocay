import pandas as pd
import sqlite3
import os

def load_presentation():
   """
   This creates the final consolidated “BIG TABLE”.
   Loads all cleaned Japan + Myanmar tables from the transformation DB.
   """

