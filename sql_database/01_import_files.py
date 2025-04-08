# IMPORTS ----
# %%
import pandas as pd

# %%
# 1.0 FILES ----

# - Pickle ----

pickle_df = pd.read_pickle("data/data_wrangled/bike_orderlines_wrangled_df.pkl")

pickle_df.info()

# - CSV ----

csv_df = pd.read_csv("data/data_wrangled/bike_orderlines_wrangled_df.csv", parse_dates = ['order_date'])

csv_df.info()

# - Excel ----

excel_df = pd.read_excel("data/data_wrangled/bike_orderlines_wrangled_df.xlsx")

excel_df.info()