"""This code reads specific variables from the Washington Post dataset and aggregates 
MME,'MME_Conversion_Factor' and 'CALC_BASE_WT_IN_GM'. It later safes the dataset to a parquet file
"""

import pandas as pd


# chunk dataset

chunk_list = []
selected_columns = [
    "BUYER_STATE",
    "BUYER_COUNTY",
    "TRANSACTION_DATE",
    "CALC_BASE_WT_IN_GM",
    "MME_Conversion_Factor",
    "MME",
]
# Create an iterable to read the dataset in chunks
chunk_iter = pd.read_csv(
    "arcos_all_washpost.tsv", sep="\t", usecols=selected_columns, chunksize=100000
)

# Iterate over the chunks and append them to the chunk_list
for chunk in chunk_iter:
    chunk_list.append(chunk)

# Concatenate all the chunks into a single DataFrame
all_states = pd.concat(chunk_list, ignore_index=True)

# aggregate MME at yeat and county level

# create year var
all_states["TRANSACTION_DATE"] = pd.to_datetime(all_states["TRANSACTION_DATE"])
all_states["YEAR"] = all_states["TRANSACTION_DATE"].dt.year

# group by state, county and year,  sum  MME CALC_BASE_WT_IN_GM
g_states = (
    all_states.groupby(["BUYER_COUNTY", "BUYER_STATE", "YEAR"])
    .agg({"MME": "sum", "MME_Conversion_Factor": "sum", "CALC_BASE_WT_IN_GM": "sum"})
    .reset_index()
)


# safe to parquet
g_states.to_parquet("county_mme.parquet")
