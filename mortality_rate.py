import pandas as pd 

with open('Data_Mortality_Rate/pop_data_cdc.txt', 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace("""---"
"Dataset: Bridged-Race Population Estimates 1990-2020"
"Query Parameters:"
"Yearly July 1st Estimates: 2003; 2004; 2005; 2006; 2007; 2008; 2009; 2010; 2011; 2012; 2013; 2014; 2015"
"Group By: State; County; Yearly July 1st Estimates"
"Show Totals: False"
"Show Zero Values: True"
"Data Table: Default"
"---"
"Help: See http://wonder.cdc.gov/wonder/help/bridged-race.html for more information."
"---"
"Query Date: Nov 20, 2023 6:21:27 AM"
"---"
"Suggested Citation: United States Department of Health and Human Services (US DHHS), Centers for Disease Control and Prevention"
"(CDC), National Center for Health Statistics (NCHS), Bridged-Race Population Estimates, United States July 1st resident"
"population by state, county, age, sex, bridged-race, and Hispanic origin. Compiled from 1990-1999 bridged-race intercensal"
"population estimates (released by NCHS on 7/26/2004); revised bridged-race 2000-2009 intercensal population estimates (released"
"by NCHS on 10/26/2012); and bridged-race Vintage 2020 (2010-2020) postcensal population estimates (released by NCHS on"
"9/22/2021). Available on CDC WONDER Online Database. Accessed at http://wonder.cdc.gov/bridged-race-v2020.html on Nov 20, 2023"
"6:21:27 AM"
"---"
Footnotes:
"1. Estimates for 1990-1999 are bridged-race intercensal population estimates of the July 1 resident population. Estimates for"
"2000-2009 are revised bridged-race intercensal estimates of the July 1 resident population. Estimates for 2010-2020 are"
"bridged-race Vintage 2020 postcensal estimates of the July 1 resident population. These estimates were prepared by the Census"
"Bureau in collaboration with NCHS."
"2. Data are not available for this area for all of the requested years. See Caveats below for more information."
"3. Data discontinuity due to county line boundary changes in requested years. See Caveats below for more information."
"---"
Caveats:
"1. 'Missing' appears when county data is not available for a certain year. This occurs because geography changes over time. New"
"counties are created and old counties are deleted or their boundaries are modified.."
"2. County geography changes over time. New counties are created and old counties are deleted or their boundaries are modified."
"The county codes and names for years 1990-1999 are based on Census 2000 geography; those for year 2000 and later are based on"
"Census 2010 geography."
"3. Chugach Census Area, AK, Alaska (FIPS code 02063) was created from the former Valdez-Cordova Census Area (FIPS code 02261)"
"effective January 2, 2019. This change was made retroactive in the data to the year 2010. Therefore population estimates for"
"Chugach Census Area are available for years 2010 and later."
"4. Copper River Census Area, AK, Alaska (FIPS code 02066) was created from the former Valdez-Cordova Census Area (FIPS code"
"02261) effective January 2, 2019. This change was made retroactive in the data to the year 2010. Therefore population estimates"
"for Copper River Census Area are available for years 2010 and later."
"5. Hoonah-Angoon Census Area, Alaska (FIPS code 02105) was created from the former Skagway-Hoonah-Angoon Census Area (FIPS code"
"02232) effective June 20, 2007. This change was made retroactive in the data to the year 2000. Therefore population estimates"
"for Hoonah-Angoon Census Area are available for years 2000 and later."
"6. Ketchikan Gateway Borough, Alaska (FIPS code 02130) annexed most of Outer Ketchikan from the former Prince of Wales-Outer"
"Ketchikan Census Area (FIPS code 02201) effective May 19, 2008. This change was made retroactive in the data to the year 2000."
"Therefore Ketchikan Gateway Borough has a discontinuity in the population estimates between 1999 and 2000 due to the addition of"
"population."
"7. About Petersburg Borough/Census Area, Alaska (FIPS code 02195): Petersburg Census Area was formed on June 1, 2008 from part"
"of the former Wrangell-Petersburg Census Area (FIPS code 02280). Effective January 3, 2013, Petersburg Census Area ceased to"
"exist; Petersburg Borough (same FIPS code 02195) was formed from part of Petersburg Census Area and part of Hoonah-Angoon Census"
"Area (02105). Population estimates for Petersburg Census Area are shown for years 2000-2009. Population estimates for Petersburg"
"Borough are shown for years after 2010."
"8. Prince of Wales-Hyder Census Area, Alaska (FIPS code 02198) was formed on June 1, 2008 from part of the former Prince of"
"Wales-Outer Ketchikan Census Area (FIPS code 02201). This change was made retroactive in the data to the year 2000. Therefore"
"population estimates for Prince of Wales-Hyder Census Area are available for years 2000 and later."
"9. Prince of Wales-Outer Ketchikan Census Area, Alaska (FIPS code 02201) ceased to exist effective June 1, 2008. The Outer"
"Ketchikan area was annexed by the Ketchikan Gateway Borough (FIPS code 02130), part was included in Wrangell City and Borough"
"(FIPS code 02275), and the remainder was renamed Prince of Wales-Hyder Census Area (FIPS code 02198). This change was made"
"retroactive in the data to the year 2000. Therefore population estimates for Prince of Wales-Outer Ketchikan Census Area are"
"only available for the years 1990-1999."
"10. Skagway Municipality, Alaska (FIPS code 02230) was created from the former Skagway-Hoonah-Angoon Census Area (FIPS code"
"02232) effective June 20, 2007. This change was made retroactive in the data to the year 2000. Therefore population estimates"
"for Skagway Municipality are available for years 2000 and later."
"11. Skagway-Hoonah-Angoon Census Area, Alaska (FIPS code 02232) ceased to exist effective June 20, 2007. Skagway Municipality"
"(FIPS code 02230) and Hoonah-Angoon Census Area (FIPS code 02105) were created from the former census area. This change was made"
"retroactive in the data to the year 2000. Therefore population estimates for Skagway-Hoonah-Angoon Census Area are only"
"available for the years 1990-1999."
"12. Valdez-Cordova Census Area, Alaska (FIPS code 02261) ceased to exist effective January 2, 2019. Chugach Census Area (FIPS"
"code 02063) and Copper River Census Area (FIPS code 02066) were created from the former census area. This change was made"
"retroactive in the data to the year 2010. Therefore population estimates for Valdez-Cordova Census Area are only available for"
"the years 1990-2009."
"13. Wade Hampton Census Area, AK (02270) was renamed to Kusilvak Census Area, AK (02158) effective July 1, 2015. This change was"
"made retroactive in the data to the year 1990."
"14. Wrangell City and Borough, Alaska (FIPS code 02275), was formed on June 1, 2008 from part of the former Wrangell-Petersburg"
"Census Area (FIPS code 02280) and part of the former Prince of Wales-Outer Ketchikan Census Area (FIPS code 02201). This change"
"was made retroactive in the data to the year 2000. Therefore population estimates for Wrangell City and Borough are available"
"for years 2000 and later."
"15. Wrangell-Petersburg Census Area, Alaska (FIPS code 02280) ceased to exist effective June 1, 2008. Petersburg Census Area"
"(FIPS code 02195) and Wrangell City and Borough (FIPS code 02275) were created from the former census area. This change was made"
"retroactive in the data to the year 2000. Therefore population estimates for Wrangell-Petersburg Census Area are only available"
"for the years 1990-1999."
"16. Broomfield County, Colorado (FIPS code 08014), was formed on November 15, 2001 from parts of Adams County (FIPS code 08001),"
"Boulder County (FIPS code 08013), Jefferson County (FIPS code 08059), and Weld County (FIPS code 08123). This change was made"
"retroactive in the data to the year 2000. Therefore population estimates for Broomfield county are available for the year 2000"
"and later. The other counties have a discontinuity in the population estimates between 1999 and 2000 due to the loss of"
"population."
"17. Shannon County, SD (46113) was renamed to Oglala Lakota County, SD (46102) effective July 1, 2015. This change was made"
"retroactive in the data to the year 1990."
"18. Bedford City, Virginia (FIPS code 51515), formerly an independent city, merged with Bedford County (FIPS code 51019) on July"
"1, 2013. This change was made retroactive in the data to the year 2010. Therefore population estimates for Bedford City are only"
"available for the years 1990-2009, and Bedford County has a discontinuity in the population estimates between 2009 and 2010 due"
"to the addition of population."
"19. Clifton Forge City, Virginia (FIPS code 51560), formerly an independent city, merged with Alleghany County (FIPS code 51005)"
"on July 1, 2001. This change was made retroactive in the data to the year 2000. Therefore population estimates for Clifton Forge"
"City are available only for the years prior to 2000. Alleghany County has a discontinuity in the population estimates between"
"1999 and 2000 due to the addition of population."
"20. South Boston City, Virginia (FIPS code 51780), formerly an independent city, merged with Halifax County (FIPS code 51083) on"
"June 30, 1995. This change was made retroactive in the data to the year 1990. Therefore, population data for South Boston City"
"have been reported with Halifax County since year 1990.""", '')

# Write the file out again
with open('Data_Mortality_Rate/pop_data_cdc.txt', 'w') as file:
  file.write(filedata)

with open('Data_Mortality_Rate/pop_data_cdc.txt', 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('"', '')

# Write the file out again
with open('Data_Mortality_Rate/pop_data_cdc.txt', 'w') as file:
  file.write(filedata)

pop_data = pd.read_csv('Data_Mortality_Rate/pop_data_cdc.txt', delimiter='\t')

pop_data[['CTYNAME','STNAME']] = pop_data['County'].str.split(',', n=1, expand=True)

pop_data['STNAME'] = pop_data['STNAME'].str.strip()

deaths = pd.read_csv('Data_Mortality_Rate/US_Vital_Stats_Deaths.csv')
deaths[['CTYNAME','STNAME']] = deaths['County'].str.split(',', n=1, expand=True)
deaths['STNAME'] = deaths['STNAME'].str.strip()

# ### Finding rows with missing values


missing_data = deaths.loc[deaths['Deaths'] == 'Missing']


missing_data[['County','Year']].drop_duplicates()

# ##### Dropping Alaska  and Virginia


deaths = deaths.loc[deaths['STNAME'] != 'AK']
deaths = deaths.loc[deaths['STNAME'] != 'VA']


deaths['Drug/Alcohol Induced Cause'].value_counts()

# #### Subset for only drug related deaths


deaths_subset = (deaths.loc[deaths['Drug/Alcohol Induced Cause'].isin(['Drug poisonings (overdose) Unintentional (X40-X44)','Drug poisonings (overdose) Suicide (X60-X64)'
                                                                       ,'Drug poisonings (overdose) Undetermined (Y10-Y14)','All other drug-induced causes'])])

deaths_subset['Drug/Alcohol Induced Cause'].value_counts()


deaths_subset = deaths_subset[['STNAME','CTYNAME','Year','Drug/Alcohol Induced Cause','Deaths']]

# #### groupby to add deaths for different categories 


deaths_subset['Deaths'] = deaths_subset['Deaths'].astype(float).astype(int)


deaths_subset['Deaths_Total'] = deaths_subset.groupby(['STNAME', 'CTYNAME','Year'])['Deaths'].transform(sum)


deaths_subset = deaths_subset[['STNAME','CTYNAME','Year','Deaths_Total']].drop_duplicates()



deaths_subset['Year'] = deaths_subset['Year'].astype('int')


# #### Impute missing values


deaths_subset.columns


deaths_subset = deaths_subset.sort_values(by=['STNAME', 'CTYNAME', 'Year'],ascending=True)



# Get unique combinations of State and CTYNAME
unique_combinations = deaths_subset[['STNAME', 'CTYNAME']].drop_duplicates()

# Convert unique combinations to a list
combinations_list = unique_combinations.values.tolist()


unique_combinations['Year'] = '2003-2015'


unique_combinations['Year'] = [[y for y in range(int(x[:4]), int(x[-4:]) + 1)] 
                        for x in unique_combinations['Year']]

unique_combinations = unique_combinations.explode('Year').reset_index(drop=True)

# #### merge unique_combinations with deaths subset 


deaths_subset.columns


data_no_missing = pd.merge(unique_combinations, deaths_subset, on=['STNAME', 'CTYNAME', 'Year'] , how=  'left')


data_no_missing = data_no_missing.fillna(5)

# ### merge with population dataset 


stats_abb = pd.read_csv('Data_Mortality_Rate/states_abb.csv')

stats_abb = stats_abb.rename(columns={'Abbreviation': 'STNAME'})


merge_data = pd.merge(data_no_missing,stats_abb,how='left',on='STNAME')


pop_data = pop_data.rename(columns={'Yearly July 1st Estimates': 'Year'})


final_merge = pd.merge(merge_data,pop_data,how='inner',on=['State','CTYNAME','Year'])


final_merge = pd.merge(merge_data,pop_data,how='inner',on=['State','CTYNAME','Year'])


final_merge['Deaths_Total'] = final_merge['Deaths_Total'].astype(float).astype(int)

final_merge['Population'] = final_merge['Population'].astype(float).astype(int)

final_merge['Mortality_Rate'] = final_merge['Deaths_Total'] / final_merge['Population']


final_merge = final_merge[['State','CTYNAME','Year','Deaths_Total','Population','Mortality_Rate']]


final_merge.to_csv('Mortality_Rate_Data.csv')


