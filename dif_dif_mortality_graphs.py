import pandas as pd
import seaborn.objects as so
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_mortality = pd.read_csv("Mortality_Rate_Data.csv")

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
    "before_policy_control": "blue",
    "after_policy_control": "blue",
    "before_policy_FL": "green",
    "after_policy_FL": "green",
}

sns.lmplot(
    x="Year",
    y="Mortality_Rate",
    hue="treatment",
    data=df_mortality_4,
    palette=palette,
    scatter=False,
    legend=False,
)
plt.axvline(x=2010, color="r", linestyle="--")
plt.title(
    "Florida vs Control States Difference-in-Differences Analysis for Mortality Rate"
)
plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.savefig("graphs_dif_dif_mortality/FL_DD_Mortality.png", bbox_inches="tight")
# plt.show()


# Washington dataset and graphs
df_mortality_WA = df_mortality[
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
    "before_policy_control": "blue",
    "after_policy_control": "blue",
    "before_policy_WA": "orange",
    "after_policy_WA": "orange",
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
plt.title(
    "Washington vs Control States Difference-in-Differences Analysis for Mortality Rate"
)
plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.savefig("graphs_dif_dif_mortality/WA_DD_Mortality.png", bbox_inches="tight")

# plt.show()

# Texas data set and graphs

df_mortality_TX = df_mortality[
    df_mortality["State"].isin(["Alabama", "Louisiana", "New Mexico", "Texas"])
]


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
    "before_policy_control": "blue",
    "after_policy_control": "blue",
    "before_policy_TX": "orange",
    "after_policy_TX": "orange",
}


sns.lmplot(
    x="Year",
    y="Mortality_Rate",
    hue="treatment",
    data=df_mortality_TX,
    palette=palette,
    scatter=False,
    legend=False,
)
plt.axvline(x=2007, color="r", linestyle="--")
plt.title(
    "Texas vs Control States Difference-in-Differences Analysis for Mortality Rate"
)
plt.xlabel("YEAR")
plt.ylabel("Mortality Rate ")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.savefig("graphs_dif_dif_mortality/TX_DD_Mortality.png", bbox_inches="tight")

# plt.show()
