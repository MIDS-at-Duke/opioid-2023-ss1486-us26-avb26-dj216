import pandas as pd

df_opiod = pd.read_parquet("county_mme.parquet")

df_pop = pd.read_csv("Data_Mortality_Rate/pop_data_cdc.txt", sep="\t")
# Add state key to mortality dataset
# Create dictionary full state names and their initials
df_pop[["COUNTY_NAME", "STATE_ID"]] = df_pop["County"].str.split(", ", n=1, expand=True)

# clean county names
df_pop["COUNTY_NAME"] = (
    df_pop["County"].str.replace(" County", "", regex=False).str.upper()
)

df_pop["COUNTY_NAME"] = df_pop["COUNTY_NAME"].str.split(",").str[0]


df_pop = df_pop[["STATE_ID", "COUNTY_NAME", "Population", "Yearly July 1st Estimates"]]

df_pop = df_pop.rename(columns={"Yearly July 1st Estimates": "YEAR"})


opiods_pop = pd.merge(
    df_opiod,
    df_pop,
    left_on=["YEAR", "BUYER_STATE", "BUYER_COUNTY"],
    right_on=["YEAR", "STATE_ID", "COUNTY_NAME"],
    how="left",
)

opiods_pop["Population"] = pd.to_numeric(opiods_pop["Population"], errors="coerce")
opiods_pop["MME_PER_CAP"] = opiods_pop["MME"] / opiods_pop["Population"]

opiods_pop.to_csv("county_mme_per_cap.csv")
