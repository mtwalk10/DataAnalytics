import pandas as pd
import sqlite3 
import plotly
db = sqlite3.connect("MotorcycleData.db")
df = pd.read_csv("/MotorcycleData.csv", header=None)
df.to_sql("Sales", db, if_exists="replace")
query = """
SELECT * 
FROM Sales;
"""
make_query(query)