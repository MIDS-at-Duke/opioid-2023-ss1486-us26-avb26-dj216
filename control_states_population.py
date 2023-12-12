<<<<<<< HEAD
# %% [markdown]
# # POPULATION  2010

# %% [markdown]
# # TEXAS 2010

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
texas_2010 = data[(data["BUYER_STATE"] == "TX") & (data["year"] == 2010)]

texas_2010.head()
texas_counties_count = texas_2010["COUNTY"].nunique()
texas_counties_count
# There were 254 counties in Texas in 2010.
texas_2010.head()
total_population_texas = texas_2010["population"].sum()
total_population_texas
# Texas population in 2010 as per this dataset was 24311891.

# %% [markdown]
# # ARIZONA

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
arizona_2010 = data[(data["BUYER_STATE"] == "AZ") & (data["year"] == 2010)]

arizona_2010.head()
arizona_counties_count = arizona_2010["COUNTY"].nunique()
arizona_counties_count
# There were 15 counties in Arizona in 2010.
arizona_2010.head()
total_population_arizona = arizona_2010["population"].sum()
total_population_arizona
# Arizona population in 2010 as per this dataset was 6246816.
arizona_2010

# %% [markdown]
# # New Mexico

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
NM_2010 = data[(data["BUYER_STATE"] == "NM") & (data["year"] == 2010)]

NM_2010.head()
NM_counties_count = NM_2010["COUNTY"].nunique()
NM_counties_count
# There were 33 counties in NM in 2010.
NM_2010.head()
total_population_NM = NM_2010["population"].sum()
total_population_NM
# New Mexico population in 2010 as per this dataset was 2013122.
NM_2010
total_population_NM
NM_counties_count

# %% [markdown]
# # Louisiana

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
LA_2010 = data[(data["BUYER_STATE"] == "LA") & (data["year"] == 2010)]

LA_2010.head()
LA_counties_count = LA_2010["COUNTY"].nunique()
LA_counties_count
# There were 64 counties in LA in 2010.
LA_2010.head()
total_population_LA = LA_2010["population"].sum()
total_population_LA
# LA population in 2010 as per this dataset was 4429940.
NM_2010
total_population_LA
LA_counties_count

total_population_LA

# %% [markdown]
# # Mississippi
#

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
MS_2010 = data[(data["BUYER_STATE"] == "MS") & (data["year"] == 2010)]

MS_2010.head()
MS_counties_count = MS_2010["COUNTY"].nunique()
MS_counties_count
# There were 82 counties in MS in 2010.
MS_2010.head()
total_population_MS = MS_2010["population"].sum()
total_population_LA
# MS population in 2010 as per this dataset was 2941991.
MS_2010
total_population_MS
MS_counties_count

total_population_MS
MS_counties_count

# %% [markdown]
# # Alabama

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
AL_2010 = data[(data["BUYER_STATE"] == "AL") & (data["year"] == 2010)]

AL_2010.head()
AL_counties_count = AL_2010["COUNTY"].nunique()
AL_counties_count
# There were 67 counties in AL in 2010.
AL_2010.head()
total_population_AL = AL_2010["population"].sum()
total_population_AL
# AL population in 2010 as per this dataset was 4712651.
MS_2010
total_population_AL
AL_counties_count

total_population_AL
AL_counties_count
total_population_AL

# %% [markdown]
# # ROUTES
# TEXAS -https://www.justice.gov/archive/ndic/pubs5/5624/5624p.pdf (Arizona connection)
# https://www.justice.gov/archive/ndic/pubs5/5624/overview.htm#:~:text=DTOs%20and%20criminal%20groups%20generally,other%20regions%20of%20the%20country.
# Alabama - https://druguse.alabama.gov/assets/files/2023AlabamaDrugThreatAssessment.pdf mexico
# MIssissipi - https://www.dps.ms.gov/sites/dps/files/2022%20MBN%20DRUG%20THREAT%20ASSESSMENT%20-%20Final.pdf (Shares with Florida - i-10) (2002)
# Louisiana - https://www.justice.gov/archive/ndic/pubs0/666/666p.pdf dominican rep(Heroin opioid) and mexico
# New Mexico - https://www.justice.gov/archive/ndic/pubs07/803/803p.pdf - Page 10 texas
# Arizona - https://www.justice.gov/archive/ndic/pubs6/6384/6384p.pdf Same route ad FL and opium almost entirely produced in South and East/west Asia
#
# Louisiana, New Mex, Alabama
#
#
#
=======
# %% [markdown]
# # POPULATION  2010

# %% [markdown]
# # TEXAS 2010

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
texas_2010 = data[(data["BUYER_STATE"] == "TX") & (data["year"] == 2010)]

texas_2010.head()
texas_counties_count = texas_2010["COUNTY"].nunique()
texas_counties_count
# There were 254 counties in Texas in 2010.
texas_2010.head()
total_population_texas = texas_2010["population"].sum()
total_population_texas
# Texas population in 2010 as per this dataset was 24311891.

# %% [markdown]
# # ARIZONA

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
arizona_2010 = data[(data["BUYER_STATE"] == "AZ") & (data["year"] == 2010)]

arizona_2010.head()
arizona_counties_count = arizona_2010["COUNTY"].nunique()
arizona_counties_count
# There were 15 counties in Arizona in 2010.
arizona_2010.head()
total_population_arizona = arizona_2010["population"].sum()
total_population_arizona
# Arizona population in 2010 as per this dataset was 6246816.
arizona_2010

# %% [markdown]
# # New Mexico

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
NM_2010 = data[(data["BUYER_STATE"] == "NM") & (data["year"] == 2010)]

NM_2010.head()
NM_counties_count = NM_2010["COUNTY"].nunique()
NM_counties_count
# There were 33 counties in NM in 2010.
NM_2010.head()
total_population_NM = NM_2010["population"].sum()
total_population_NM
# New Mexico population in 2010 as per this dataset was 2013122.
NM_2010
total_population_NM
NM_counties_count

# %% [markdown]
# # Louisiana

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
LA_2010 = data[(data["BUYER_STATE"] == "LA") & (data["year"] == 2010)]

LA_2010.head()
LA_counties_count = LA_2010["COUNTY"].nunique()
LA_counties_count
# There were 64 counties in LA in 2010.
LA_2010.head()
total_population_LA = LA_2010["population"].sum()
total_population_LA
# LA population in 2010 as per this dataset was 4429940.
NM_2010
total_population_LA
LA_counties_count

total_population_LA

# %% [markdown]
# # Mississippi
#

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
MS_2010 = data[(data["BUYER_STATE"] == "MS") & (data["year"] == 2010)]

MS_2010.head()
MS_counties_count = MS_2010["COUNTY"].nunique()
MS_counties_count
# There were 82 counties in MS in 2010.
MS_2010.head()
total_population_MS = MS_2010["population"].sum()
total_population_LA
# MS population in 2010 as per this dataset was 2941991.
MS_2010
total_population_MS
MS_counties_count

total_population_MS
MS_counties_count

# %% [markdown]
# # Alabama

# %%
import pandas as pd

data = pd.read_csv(
    "https://github.com/wpinvestigative/arcos-api/raw/master/data/pop_counties_20062014.csv"
)
data.head()

# Corrected line for filtering Texas and the year 2010
AL_2010 = data[(data["BUYER_STATE"] == "AL") & (data["year"] == 2010)]

AL_2010.head()
AL_counties_count = AL_2010["COUNTY"].nunique()
AL_counties_count
# There were 67 counties in AL in 2010.
AL_2010.head()
total_population_AL = AL_2010["population"].sum()
total_population_AL
# AL population in 2010 as per this dataset was 4712651.
MS_2010
total_population_AL
AL_counties_count

total_population_AL
AL_counties_count
total_population_AL

# %% [markdown]
# # ROUTES
# TEXAS -https://www.justice.gov/archive/ndic/pubs5/5624/5624p.pdf (Arizona connection)
# https://www.justice.gov/archive/ndic/pubs5/5624/overview.htm#:~:text=DTOs%20and%20criminal%20groups%20generally,other%20regions%20of%20the%20country.
# Alabama - https://druguse.alabama.gov/assets/files/2023AlabamaDrugThreatAssessment.pdf mexico
# MIssissipi - https://www.dps.ms.gov/sites/dps/files/2022%20MBN%20DRUG%20THREAT%20ASSESSMENT%20-%20Final.pdf (Shares with Florida - i-10) (2002)
# Louisiana - https://www.justice.gov/archive/ndic/pubs0/666/666p.pdf dominican rep(Heroin opioid) and mexico
# New Mexico - https://www.justice.gov/archive/ndic/pubs07/803/803p.pdf - Page 10 texas
# Arizona - https://www.justice.gov/archive/ndic/pubs6/6384/6384p.pdf Same route ad FL and opium almost entirely produced in South and East/west Asia
#
# Louisiana, New Mex, Alabama
#
#
#
>>>>>>> b8bebe5248978ab272fdd35ad9f60f8da761c881
