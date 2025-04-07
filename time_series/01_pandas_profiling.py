# %%
# IMPORTS

import pandas as pd

from ydata_profiling import ProfileReport, profile_report

from my_panda_extensions.database import collect_data

df = collect_data()
df


# %%
# PANDAS PROFILING

# Get a Profile

profile = ProfileReport(
    df = df
)

profile

# %%
# Sampling - Big Datasets

df.profile_report()

# %%
df.sample(frac = 0.5).profile_report()

# %%
df.profile_report(dark_mode = True)

# Pandas Helper
# ?pd.DataFrame.profile_report

# %%
# Saving Output

df.profile_report().to_file("reports/profile_report.html")

# VSCode Extension - Browser Preview




# %%
