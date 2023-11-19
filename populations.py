import pandas as pd

"data_2006_2010"
a = pd.read_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/Population_2006_2010.csv", encoding = 'latin-1')
"data_2010_2015"
b = pd.read_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/Population_2010_2015.csv", encoding = 'latin-1')

"Below is trying to find if these datasets differ in statename"
# print (a[~a['STNAME'].isin(b['STNAME'])])
# print (b[~b['STNAME'].isin(a['STNAME'])])

"Below is trying to find if these datasets differ in countyname"

"This effectively gives you the county names in a that are not in b"

# print (a[~a['CTYNAME'].isin(b['CTYNAME'])])
print(a.loc[[88,94,1161,2963]])
# 88: Alaska	North Slope Borough
# 94: Alaska	Southeast Fairbanks Census Area
# 1161: Louisiana	Lafayette Parish
# 2963: Virginia	York County



" This effectively gives you the county names in b that are not in a"
# print (b[~b['CTYNAME'].isin(a['CTYNAME'])])
print(b.loc[[83,89,1161,2454]])
# 83: Alaska	Ketchikan Gateway Borough
# 89: Alaska	North Slope Borough
# 1161: Louisiana	Lafayette Parish
# 2454: South Dakota	Minnehaha County





# print(a.shape)
# print(b.shape)
x = pd.merge(a, b, on=['STNAME', 'CTYNAME'])
x.to_csv("/workspaces/opioid-2023-ss1486-us26-avb26-dj216/data_pop/pop_merge.csv", index=False)
# print(x.head())
# print(x.shape)



