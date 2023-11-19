from shlex import join
import pandas as pd
import numpy as np

"data_2006_2010"
a = pd.read_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/Population_2006_2010.csv", encoding = 'latin-1')
a = a[['STNAME', 'CTYNAME', 'POPESTIMATE2006', 'POPESTIMATE2007', 'POPESTIMATE2008', 'POPESTIMATE2009']]

"data_2010_2015"
b = pd.read_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/Population_2010_2015.csv", encoding = 'latin-1')
b = b[['STNAME', 'CTYNAME', "POPESTIMATE2010",'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]

"Below is trying to find if these datasets differ in statename"
# print (a[~a['STNAME'].isin(b['STNAME'])])
# print (b[~b['STNAME'].isin(a['STNAME'])])

"Below is trying to find if these datasets differ in countyname"

"This effectively gives you the county names in a that are not in b"

# print (a[~a['CTYNAME'].isin(b['CTYNAME'])])
# print(a.loc[[88,94,1161,2963]])
# 88: Alaska	North Slope Borough
# 94: Alaska	Southeast Fairbanks Census Area
# 1161: Louisiana	Lafayette Parish
# 2963: Virginia	York County



" This effectively gives you the county names in b that are not in a"
# print (b[~b['CTYNAME'].isin(a['CTYNAME'])])
# print(b.loc[[83,89,1161,2454]])
a['CTYNAME'] = np.where((a['STNAME'] == 'South Dakota') & (a['CTYNAME'] == 'Shannon County') , "Oglala Lakota County", a['CTYNAME'])
#a['CTYNAME'] = a['CTYNAME'].replace({'Shannon County' : 'Oglala Lakota County'})
a['CTYNAME'] = a['CTYNAME'].replace({'La Salle Parish': 'LaSalle Parish' })
a['CTYNAME'] = a['CTYNAME'].replace({ 'Petersburg Census Area' : 'Petersburg Borough'})
a['CTYNAME'] = a['CTYNAME'].replace({'Wade Hampton Census Area': 'Kusilvak Census Area'})


#drop Bedford city from a

a.drop(a[a['CTYNAME'] == 'Bedford city'].index, inplace=True)



# 83: Alaska	Ketchikan Gateway Borough
# 89: Alaska	North Slope Borough
# 1161: Louisiana	Lafayette Parish
# 2454: South Dakota	Minnehaha County





print(a.shape)
print(b.shape)
x = pd.merge(a, b, on=['STNAME', 'CTYNAME'], how='inner')

x.drop_duplicates(keep=False, inplace=True) 


# x.to_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/pop_merge.csv", index=False)
# print(x.head())
print(x.shape)

id_vars = ["STNAME", "CTYNAME"]
df = x.melt(id_vars =id_vars)
df = df.rename(columns = {"variable": "Year", "value": "Population"})



# print (x[~x['CTYNAME'].isin(b['CTYNAME'])])
# print (x[~x['CTYNAME'].isin(a['CTYNAME'])])

df["Year"] = df["Year"].str.replace("POPESTIMATE", "")
print(df.head())
df.to_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/pop_merge.csv", index=False)
