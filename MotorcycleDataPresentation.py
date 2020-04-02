# - Import Packages
import pandas as pd
import sqlite3 
import plotly


# - Import Data into Database
db = sqlite3.connect("MotorcycleData.db")
df = pd.read_csv('MotorcycleData.csv', encoding='cp1252')

df.to_sql("Sales", db, if_exists="replace")


# - Display Rough Data
def make_query(query): 
    return pd.read_sql_query(query,db)    

query = """
SELECT * 
FROM Sales;
"""
make_query(query)


# - Display Cleaned Data
query = """
SELECT Condition, Price, Model_Year AS "Year", Exterior_Color AS "Color", Make 
FROM Sales;
"""
make_query(query)


# - Basic Data Manipulation - Total Sales
query = """
SELECT '$' || SUM(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)) AS "Total Sales"
FROM Sales;
"""
make_query(query)


# - Basic Data Manipulation - Average Sales
query = """
SELECT '$' || ROUND(AVG(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)), 2) AS "Average Price"
FROM Sales;
"""
make_query(query)



# - Basic Data Manipulation - Number of Sales by Make 
query = """
SELECT COUNT(Price), Make 
FROM Sales
GROUP BY Make;
"""
make_query(query)