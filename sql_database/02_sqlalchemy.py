# %%
# IMPORTS ----

import pandas as pd
import sqlalchemy as sql
from sqlalchemy import inspect, Inspector

import os

os.mkdir("database")

# %%
# CREATING A DATABASE ----

# Instatiate a database

engine = sql.create_engine("sqlite:///database/bike_orders_database.sqlite")

conn = engine.connect()

# %%
# Read Excel Files

bikes_df = pd.read_excel("data/raw/bikes.xlsx")

bikeshops_df = pd.read_excel("data/raw/bikeshops.xlsx")

orderlines_df = pd.read_excel("data/raw/orderlines.xlsx")

# %%
# Create Tables

bikes_df.to_sql("bikes", con = engine, if_exists = "replace")
pd.read_sql("SELECT * FROM bikes", con = engine)

bikeshops_df.to_sql("bikeshops", con = engine, if_exists = "replace")
pd.read_sql("SELECT * FROM bikeshops", con = engine)

orderlines_df \
    .iloc[: , 1:] \
    .to_sql("orderlines", con = engine, if_exists = "replace")
pd.read_sql("SELECT * FROM orderlines", con = engine) 

# %%
# Close Connection

conn.close()

# %%
# RECONNECTING TO THE DATABASE 

# Connecting is the same as creating

engine = sql.create_engine("sqlite:///database/bike_orders_database.sqlite")

conn = engine.connect()

# %%
# GETTING DATA FROM THE DATABASE

# Get the table names

inspector = sql.inspect(conn)

inspector.get_schema_names()

inspector.get_table_names('main')

# %%
# Read the data

table = inspector.get_table_names()
pd.read_sql(f"SELECT * FROM {table[2]}", con = engine)

# %%
# Close Connection

conn.close()
