import pandas as pd
import sqlite3 
import plotly

db = sqlite3.connect("MotorcycleData.db")
df = pd.read_csv('MotorcycleData.csv', encoding='cp1252')

df.to_sql("Sales", db, if_exists="replace")

def make_query(query): 
    return pd.read_sql_query(query,db)
    

query = """
SELECT * 
FROM Sales;
"""
make_query(query)