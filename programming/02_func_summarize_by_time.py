# Imports

import pandas as pd
import numpy as np
from pandas.core import groupby

from my_panda_extensions.database import collect_data

df = collect_data()

# %%
# WHAT WE WANT TO STREAMLINE



df[['category_2', 'order_date', 'total_price']] \
    .groupby( 
        ['category_2',pd.Grouper(key='order_date',freq = 'Q')]
    ) \
    .agg(np.sum) \
    .unstack("category_2") \
    .reset_index() \
    .assign(order_date = lambda x: x['order_date'].dt.to_period()) \
    .set_index("order_date") 
    
# Matt code  
df[['category_2', 'order_date', 'total_price']] \
    .set_index('order_date') \
    .groupby('category_2') \
    .resample('M', kind = 'period') \
    .agg(np.sum) \
    .unstack("category_2") \
    .reset_index() \
    .assign(order_date = lambda x: x['order_date'].dt.to_period()) \
    .set_index("order_date")

# %%
# BUILDING SUMMARIZE BY TIME

def summarize_by_time(
    data, date_column, value_column, 
    groups = None, rule = "D"
):


# ADDING TO OUR TIME SERIES MODULE

