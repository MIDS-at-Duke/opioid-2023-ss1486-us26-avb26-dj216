import pandas as pd
import seaborn.objects as so
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_mortality = pd.read_csv(
    "/Users/danielajimenez/opioid-2023-ss1486-us26-avb26-dj216/20_intermediate_files/county_level_mortality_rate.csv"
)
# df_mortality["Mortality_Rate"] *= 100000

# Florida dataset and graphs
df_mortality_4 = df_mortality[
    df_mortality["State"].isin(["Alabama", "Arizona", "Missouri", "Florida"])
]

conditions = [
    (df_mortality_4["Year"] < 2010) & (df_mortality_4["State"] != "Florida"),
    (df_mortality_4["Year"] >= 2010) & (df_mortality_4["State"] != "Florida"),
    (df_mortality_4["Year"] < 2010) & (df_mortality_4["State"] == "Florida"),
    (df_mortality_4["Year"] >= 2010) & (df_mortality_4["State"] == "Florida"),
]
choices = [
    "before_policy_control",
    "after_policy_control",
    "before_policy_FL",
    "after_policy_FL",
]

df_mortality_4["treatment"] = np.select(conditions, choices, default="Other")

plt.clf()

palette = {
    "before_policy_control": "red",
    "after_policy_control": "red",
    "before_policy_FL": "blue",
    "after_policy_FL": "blue",
}

sns.lmplot(
    x="Year",
    y="Mortality_Rate_Per_100k",
    hue="treatment",
    data=df_mortality_4,
    palette=palette,
    scatter=False,
    legend=False,
)
plt.axvline(x=2010, color="r", linestyle="--")

plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
# file_path = (
#    r"opioid-2023-ss1486-us26-avb26-dj216\graphs_dif_dif_mortality\florida_dif.png"
# )
# plt.savefig(file_path, bbox_inches="tight")
plt.show()


# Washington dataset and graphs

df_mortality_WA = df_mortality[df_mortality["Year"] >= 2006]


df_mortality_WA = df_mortality_WA[
    df_mortality["State"].isin(["Idaho", "Oregon", "Montana", "Washington"])
]


conditions = [
    (df_mortality_WA["Year"] < 2012) & (df_mortality_WA["State"] != "Washington"),
    (df_mortality_WA["Year"] >= 2012) & (df_mortality_WA["State"] != "Washington"),
    (df_mortality_WA["Year"] < 2012) & (df_mortality_WA["State"] == "Washington"),
    (df_mortality_WA["Year"] >= 2012) & (df_mortality_WA["State"] == "Washington"),
]
choices = [
    "before_policy_control",
    "after_policy_control",
    "before_policy_WA",
    "after_policy_WA",
]

df_mortality_WA["treatment"] = np.select(conditions, choices, default="Other")


plt.clf()
palette = {
    "before_policy_control": "red",
    "after_policy_control": "red",
    "before_policy_WA": "blue",
    "after_policy_WA": "blue",
}


sns.lmplot(
    x="Year",
    y="Mortality_Rate",
    hue="treatment",
    data=df_mortality_WA,
    palette=palette,
    scatter=False,
    legend=False,
)
plt.axvline(x=2012, color="r", linestyle="--")

plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)

plt.show()


# file_path = (
#    r"opioid-2023-ss1486-us26-avb26-dj216\graphs_dif_dif_mortality\washington_dif.png"
# )
# plt.savefig(file_path, bbox_inches="tight")

# Texas data set and graphs

df_mortality_TX = df_mortality[
    df_mortality["State"].isin(["Alabama", "Louisiana", "New Mexico", "Texas"])
]

df_mortality_TX = df_mortality_TX[df_mortality_TX["Year"] < 2011]
conditions = [
    (df_mortality_TX["Year"] < 2007) & (df_mortality_TX["State"] != "Texas"),
    (df_mortality_TX["Year"] >= 2007) & (df_mortality_TX["State"] != "Texas"),
    (df_mortality_TX["Year"] < 2007) & (df_mortality_TX["State"] == "Texas"),
    (df_mortality_TX["Year"] >= 2007) & (df_mortality_TX["State"] == "Texas"),
]
choices = [
    "before_policy_control",
    "after_policy_control",
    "before_policy_TX",
    "after_policy_TX",
]

df_mortality_TX["treatment"] = np.select(conditions, choices, default="Other")

plt.clf()
palette = {
    "before_policy_control": "red",
    "after_policy_control": "red",
    "before_policy_TX": "blue",
    "after_policy_TX": "blue",
}


sns.lmplot(
    x="Year",
    y="Mortality_Rate_Per_100k",
    hue="treatment",
    data=df_mortality_TX,
    palette=palette,
    scatter=False,
    legend=False,
)
plt.axvline(x=2007, color="r", linestyle="--")

plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)

# file_path = (
#    r"opioid-2023-ss1486-us26-avb26-dj216\graphs_dif_dif_mortality\texas_dif.png"
# )
# plt.savefig(file_path, bbox_inches="tight")


plt.show()
