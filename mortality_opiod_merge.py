import pandas as pd

import pandas as pd

# Read a Parquet file
df = pd.read_parquet("C:\\Users\\admin\\Downloads\\county_mme.parquet")
# print(df)


import pandas as pd

# Provide the correct local file path
file_path = r"C:\Users\admin\Downloads\Mortality_Rate_Data.csv"

# Read the CSV file into a Pandas DataFrame
df2 = pd.read_csv(file_path)
# print(df2)
import pandas as pd

# Assuming df2 is your second table

# Create a mapping between full state names and their initials
state_mapping = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Add a new column 'State_Initials' to the second table
df2["State_Initials"] = df2["State"].map(state_mapping)

# Display the updated DataFrame with the new column
# print(df2)
# Assuming df2 is your DataFrame
# print(df2.head(50))
# print(df)

# Assuming df1 is the first DataFrame and df2 is the second DataFrame with State Initials column
merged_df = pd.merge(
    df,
    df2,
    left_on=["BUYER_STATE", "YEAR"],
    right_on=["State_Initials", "Year"],
    how="inner",
)

# Assuming df is your DataFrame
south_carolina_buyer_counties = df[df["BUYER_STATE"] == "SC"]["BUYER_COUNTY"].unique()

# Display the unique BUYER_COUNTY values for South Carolina
# print(south_carolina_buyer_counties)

# Assuming df2 is your DataFrame
south_carolina_counties = df2[df2["State"] == "South Carolina"]["CTYNAME"].unique()

# Display the unique CTYNAME values for South Carolina
# print(south_carolina_counties)
# print(merged_df)

# Assuming df2 is your DataFrame
south_carolina_counties = df2[df2["State"] == "South Carolina"]["CTYNAME"].unique()

# Display the unique CTYNAME values for South Carolina
# print(south_carolina_counties)
# Assuming df is your DataFrame
south_carolina_buyer_counties = df[df["BUYER_STATE"] == "SC"]["BUYER_COUNTY"].unique()

# Display the unique BUYER_COUNTY values for South Carolina
# print(south_carolina_buyer_counties)

# print(df2)

south_carolina_counties = df2[df2["State"] == "South Carolina"]["CTYNAME"].unique()
# print(south_carolina_counties)

# Assuming df2 is your DataFrame, dropping the "County" and turning the first word into upper case.
df2["CTYNAME"] = df2["CTYNAME"].apply(lambda x: x.split()[0].upper())
print(df2)


# Extract unique county names from the modified 'CTYNAME' in df2
df2_counties = df2["CTYNAME"].unique()

# Extract unique county names from 'BUYER_COUNTY' in df
df_counties = df["BUYER_COUNTY"].unique()

# Find common counties
common_counties = set(df2_counties) & set(df_counties)

# Print the number of common counties
print(f"Number of common counties: {len(common_counties)}")

# Print the common counties
print("Common counties:", common_counties)
# Find uncommon counties
# uncommon_counties = set(df2_counties) ^ set(df_counties)

# Print the number of uncommon counties
# print(f"Number of uncommon counties: {len(uncommon_counties)}")

# Print the uncommon counties
# print("Uncommon counties:", uncommon_counties)
