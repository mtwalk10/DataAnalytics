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


# - Basic Data Manipulation - Total Sales By Make
query = """
SELECT '$' || SUM(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)) AS "Total Sales by Make", Make
FROM Sales
GROUP BY Make
"""
make_query(query)


# - Basic Data Manipulation - Average Sales By Make
query = """
SELECT '$' || ROUND(AVG(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)), 2) AS "Average Price by Make", Make
FROM Sales
GROUP BY Make
"""
make_query(query)


# - Data Manipulation - Finding the Three Best Selling Makes (By Number of Sales)

query = """
SELECT COUNT(Price) AS "Number of Sales", Make 
FROM Sales
GROUP BY Make
ORDER BY COUNT(Price) DESC
LIMIT 3;
"""
make_query(query)


# - Data Manipulation - Finding the Three Best Selling Makes (By Total Value of Sales)

query = """
SELECT '$' || SUM(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)) AS "Total Sales by Make", Make
FROM Sales
GROUP BY Make
ORDER BY SUM(CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int)) DESC
LIMIT 3;
"""
make_query(query)


# - Data Manipulation - Finding the Three Highest Individual Sales
query = """
SELECT '$' || CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int) AS "Sale Price", Make, Model_Year AS "Year", 
Mileage, Exterior_Color AS "COLOR"
FROM Sales
GROUP BY Make
ORDER BY CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int) DESC
LIMIT 3;
"""
make_query(query)


# - Data Manipulation - Finding the Three Oldest Bikes Sold
query = """
SELECT '$' || CAST(REPLACE(REPLACE(Price, '$',''), ',','') AS int) AS "Sale Price", Make, Model_Year AS "Year"
FROM Sales
ORDER BY Model_Year
LIMIT 3
"""
make_query(query)


# - Data Manipulation - Finding the Three Most Common Colors of Bike Sold
query = """
SELECT COUNT(Exterior_Color) AS "Number of Bikes Sold", Exterior_Color AS "Color"
FROM Sales
GROUP BY Exterior_Color
ORDER BY COUNT(Exterior_Color) DESC
LIMIT 3
"""
make_query(query)



# - Data Manipulation - Finding the Most Popular Model for each Make
query = """
SELECT Make, Model AS "Most Popular Model", COUNT(Model) AS "Number of Bikes Sold"
FROM Sales
GROUP BY Make
"""
make_query(query)

