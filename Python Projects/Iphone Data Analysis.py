# Databricks notebook source
# Use %pip instead of !pip for Databricks Notebooks
%pip install pandas

# COMMAND ----------

# Import pandas
import pandas as pd

# COMMAND ----------

# Read CSV file using pandas
df = pd.read_csv('apple_products.csv')
df.head()

# COMMAND ----------

df.count()

# COMMAND ----------

print(df['Mrp'].max())
print(df['Mrp'].min())

# COMMAND ----------

df[df['Mrp'] == df['Mrp'].max()]
