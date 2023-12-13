import pandas as pd

# Read death and population data
population_data = pd.read_csv('Data_Mortality_Rate/pop_data_cdc.txt', delimiter='\t')
population_data[['CTYNAME', 'STNAME']] = population_data['County'].str.split(',', n=1, expand=True)
population_data['STNAME'] = population_data['STNAME'].str.strip()

deaths = pd.read_csv('Data_Mortality_Rate/US_Vital_Stats_Deaths.csv')
deaths[['CTYNAME', 'STNAME']] = deaths['County'].str.split(',', n=1, expand=True)
deaths['STNAME'] = deaths['STNAME'].str.strip()

# Data Cleaning
# Dropping Alaska and Virginia
deaths = deaths.loc[~deaths['STNAME'].isin(['AK', 'VA'])]

# Subsetting data for relevant causes
relevant_causes = ['Drug poisonings (overdose) Unintentional (X40-X44)', 'Drug poisonings (overdose) Suicide (X60-X64)',
                   'Drug poisonings (overdose) Undetermined (Y10-Y14)', 'All other drug-induced causes']
deaths_subset = deaths[deaths['Drug/Alcohol Induced Cause'].isin(relevant_causes)]
deaths_subset = deaths_subset[['STNAME', 'CTYNAME', 'Year', 'Drug/Alcohol Induced Cause', 'Deaths']]

# Rename population column
population_data.rename(columns={'Yearly July 1st Estimates': 'Year'}, inplace=True)

# Merging death and population data
merged_data = pd.merge(deaths_subset, population_data, on=['STNAME', 'CTYNAME', 'Year'], how='left')

# Calculating Mortality Rate (County Level)
county_level_data = merged_data.copy()
county_level_data['Deaths'] = county_level_data['Deaths'].astype(float).astype(int)
county_level_data['Population'] = county_level_data['Population'].astype(int)
county_level_data["Mortality_Rate"] = county_level_data["Deaths"] / county_level_data["Population"]

# Mortality Rate (State Level)
state_level_data = county_level_data.groupby(["State", "Year", "Drug/Alcohol Induced Cause"]).agg(
    {"Deaths": "sum", "Population": "sum"}).reset_index()
state_level_data = state_level_data[state_level_data["Drug/Alcohol Induced Cause"] == "Drug poisonings (overdose) Unintentional (X40-X44)"]
state_level_data["State_Mortality_Rate"] = state_level_data["Deaths"] / state_level_data["Population"]

# Merge State Mortality Rate with State-County list
state_county_list = population_data[["State", "County", "County Code", "Year"]].drop_duplicates()
merged_state_data = pd.merge(state_county_list, state_level_data, on=["State", "Year"], how="left", indicator=True)
merged_state_data = merged_state_data[merged_state_data["_merge"] == "both"]

# Cleaning the merged data
cleaned_data = merged_state_data[["State", "County", "County Code", "Year", "Drug/Alcohol Induced Cause", "State_Mortality_Rate"]]

# Merge with county level data
merged_county_data = pd.merge(cleaned_data, county_level_data, on=["State", "County", "County Code", "Year", "Drug/Alcohol Induced Cause"], how="left", indicator=True, validate="1:1")

# Remap with population data to get county population
merged_county_population = pd.merge(merged_county_data, population_data[["County Code", "Year", "Population"]], on=["County Code", "Year"], how="left", validate="m:1", indicator="merge2")

# Calculate the Final Deaths
merged_county_population['State_Mortality_Rate'] = pd.to_numeric(merged_county_population['State_Mortality_Rate'], errors='coerce')
merged_county_population['Population_y'] = pd.to_numeric(merged_county_population['Population_y'], errors='coerce')
merged_county_population['Deaths2'] = merged_county_population.apply(
    lambda row: min(int(row['Population_y'] * row['State_Mortality_Rate']), 9) if pd.isna(row['Deaths']) else row['Deaths'], axis=1)

# Clean the dataset
cleaned_dataset = merged_county_population[["State", "County", "County Code", "Year", "Drug/Alcohol Induced Cause", "Deaths2", "Population_y"]]
cleaned_dataset = cleaned_dataset.rename(columns={"Population_y": "Population", "Deaths2": "Deaths"})

# Aggregate at County level and calculate Final Mortality Rate (County Level)
final_county_level_data = cleaned_dataset.groupby(["State", "County", "County Code", "Year"]).agg({"Deaths": "sum", "Population": "mean"}).reset_index()
final_county_level_data["Mortality_Rate"] = final_county_level_data["Deaths"] / final_county_level_data["Population"]
final_county_level_data['Mortality_Rate_Per_100k'] = final_county_level_data['Mortality_Rate'] * 100000

print(final_county_level_data.head(10))

# Export as csv for plotting
final_county_level_data.to_csv('county_level_mortality_rate.csv', index=False)

"""
The code provided performs several data processing tasks on mortality data. It begins by reading and preparing two 
datasets: one containing population estimates ('pop_data') and another recording deaths ('deaths'). The process involves
data cleaning steps like removing specific states from the death records. Subsetting focuses on drug/alcohol-induced
death causes and merges relevant columns for consistency. Through merging these datasets based on state, county, 
and year, the code creates a unified dataset. Mortality rates at both county and state levels are computed by dividing 
deaths by the population, addressing drug-induced deaths specifically for unintentional drug poisonings.
Missing death records are handled using a function called 'calculate_deaths,' which utilizes the state mortality 
rate and county population. This function fills in missing values by estimating deaths; however, it caps the imputed 
deaths at 9 to maintain realistic figures. Finally, the code aggregates data at the county level and computes final 
mortality rates per 100,000 population, providing a comprehensive analysis of mortality rates considering population
size and cause-specific death rates.
"""