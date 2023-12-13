import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Morphine Milligram Equivalent (MME) Conversion (mg)

"""Load the data into a Pandas dataframe."""
file_path = "/Users/danielajimenez/opioid-2023-ss1486-us26-avb26-dj216/20_intermediate_files/county_mme_per_cap.csv"
shipments = pd.read_csv(file_path)

## Prepare dataset for graphs
year_mask = (shipments["YEAR"] > 2006) & (shipments["YEAR"] < 2013)
shipments_FL = shipments.loc[year_mask]
shipments_FL = shipments[shipments["BUYER_STATE"].isin(["AL", "AZ", "MS", "FL"])]
shipments_TX = shipments[shipments["BUYER_STATE"].isin(["AL", "AZ", "MS", "TX"])]
shipments_WA = shipments[shipments["BUYER_STATE"].isin(["AL", "AZ", "MS", "WA"])]


"""Florida """

if shipments_FL["BUYER_STATE"].isin(["AL", "AZ", "MS"]).any():
    shipments_FL.loc[
        shipments_FL["BUYER_STATE"].isin(["AL", "AZ", "MS"]), "BUYER_STATE"
    ] = "control"

final_df = shipments_FL.sort_values("YEAR")[
    ["YEAR", "BUYER_STATE", "BUYER_COUNTY", "MME", "MME_PER_CAP"]
]
print(final_df)

final_df["intervention"] = 0
final_df["intervention"] = final_df.intervention.where(final_df["YEAR"] < 2010, 1)
final_df["state_class"] = np.where(final_df["BUYER_STATE"] == "FL", "1", "0")


print(final_df.head())


conditions = [
    (final_df["YEAR"] < 2010) & (final_df["BUYER_STATE"] != "FL"),
    (final_df["YEAR"] >= 2010) & (final_df["BUYER_STATE"] != "FL"),
    (final_df["YEAR"] < 2010) & (final_df["BUYER_STATE"] == "FL"),
    (final_df["YEAR"] >= 2010) & (final_df["BUYER_STATE"] == "FL"),
]
choices = [
    "before_policy_control",
    "after_policy_control",
    "before_policy_FL",
    "after_policy_FL",
]

palette = {
    "before_policy_control": "red",
    "after_policy_control": "red",
    "before_policy_FL": "blue",
    "after_policy_FL": "blue",
}

final_df["policy_change"] = np.select(conditions, choices, default="other")
print(final_df.head())


# Florida Graph
plt.figure(figsize=(10, 6))
sns.lmplot(
    data=final_df,
    x="YEAR",
    y="MME_PER_CAP",
    hue="policy_change",
    palette=palette,
    hue_order=choices,
    scatter=False,
    legend=False,
)
plt.axvline(x=2010, color="r", linestyle="--")
plt.title("")
plt.xlabel("YEAR")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.ylabel("Morphine Miligram Equivalent per Capita")
plt.savefig(
    "figures/florida_diff_v2.png",
    bbox_inches="tight",
)
plt.show()


""" WASHINGTON"""
year_wa_mask = (shipments["YEAR"] > 2005) & (shipments["YEAR"] < 2015)
shipments_WA = shipments.loc[year_wa_mask]

if shipments_WA["BUYER_STATE"].isin(["ID", "OR", "MT"]).any():
    shipments_WA.loc[
        shipments_WA["BUYER_STATE"].isin(["ID", "OR", "MT"]), "BUYER_STATE"
    ] = "control"


final_wa_df = shipments_WA.sort_values("YEAR")[
    ["YEAR", "BUYER_STATE", "BUYER_COUNTY", "MME", "MME_PER_CAP"]
]
# print(final_df)

final_wa_df["intervention"] = 0
final_wa_df["intervention"] = final_wa_df.intervention.where(
    final_wa_df["YEAR"] < 2012, 1
)
final_wa_df["state_class"] = np.where(final_wa_df["BUYER_STATE"] == "WA", "1", "0")

# Create a new column 'group' that categorizes the data into four groups
conditions = [
    (final_wa_df["YEAR"] < 2012) & (final_wa_df["BUYER_STATE"] != "WA"),
    (final_wa_df["YEAR"] >= 2012) & (final_wa_df["BUYER_STATE"] != "WA"),
    (final_wa_df["YEAR"] < 2012) & (final_wa_df["BUYER_STATE"] == "WA"),
    (final_wa_df["YEAR"] >= 2012) & (final_wa_df["BUYER_STATE"] == "WA"),
]
choices = [
    "before_policy_control",
    "after_policy_control",
    "before_policy_WA",
    "after_policy_WA",
]

palette = {
    "before_policy_control": "red",
    "after_policy_control": "red",
    "before_policy_WA": "blue",
    "after_policy_WA": "blue",
}

final_wa_df["policy_change"] = np.select(conditions, choices, default="other")
print(final_wa_df.head())

plt.figure(figsize=(30, 20))
sns.lmplot(
    data=final_wa_df,
    x="YEAR",
    y="MME_PER_CAP",
    hue="policy_change",
    palette=palette,
    hue_order=choices,
    scatter=False,
    legend=False,
    ci=68,
)
plt.axvline(x=2012, color="r", linestyle="--")
plt.title("")
plt.xlabel("YEAR")
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.ylabel("Morphine Miligram Equivalent per Capita")
plt.savefig(
    "figures/washington_diff_v2.png",
    bbox_inches="tight",
)
plt.show()

""" TEXAS"""
# year_tx_mask = (shipments["YEAR"] > 2004) & (shipments["YEAR"] < 2010)
# shipments_TX = shipments.loc[year_tx_mask]
# if shipments_TX["BUYER_STATE"].isin(["AL", "LA", "NM"]).any():
#     shipments_TX.loc[
#         shipments_TX["BUYER_STATE"].isin(["AL", "LA", "NM"]), "BUYER_STATE"
#     ] = "control"

# # print(shipments.head())


# # new_df = shipments[["YEAR", "BUYER_STATE", "BUYER_COUNTY", "MME"]].copy()
# # print(new_df)
# # pivot_df = shipments.pivot_table(index='YEAR', columns='State_Class', values='MME', aggfunc='mean')
# # print(pivot_df.head())

# # print(new_df.head())
# # final_df = shipments.pivot_table(index='YEAR', columns='BUYER_STATE', values='MME', aggfunc='mean')
# # print(final_df)
# # final_df = shipments.groupby(["YEAR", "BUYER_STATE", "BUYER_COUNTY"])["MME"]
# # Python
# # Python
# final_tx_df = shipments_TX.sort_values("YEAR")[
#     ["YEAR", "BUYER_STATE", "BUYER_COUNTY", "MME"]
# ]
# print(final_tx_df)

# final_tx_df["intervention"] = 0
# final_tx_df["intervention"] = final_df.intervention.where(final_df["YEAR"] < 2007, 1)
# final_tx_df["state_class"] = np.where(final_df["BUYER_STATE"] == "TX", "1", "0")


# print(final_tx_df.head())


# # model = "MME ~ state_class + intervention + intervention * state_class"
# # mod = smf.ols(formula=model, data=final_df)
# # res = mod.fit()
# # print(res.summary())


# # result = final_df.groupby('intervention').mean()
# # # print(result)

# # result.columns = ['control', 'treatment']
# # print(result['control'] - result['treatment'])
# # print((result['treatment'] - result['control']).diff())


# # MME = state_class +


# # sns.scatterplot(x="YEAR", y="MME", data=final_tx_df, hue="BUYER_COUNTY")
# # plt.xlabel("YEAR")
# # plt.ylabel("Mean MME")
# # plt.title("Difference-in-Differences Plot")
# # plt.show()


# # Create a new column 'group' that categorizes the data into four groups
# conditions = [
#     (final_tx_df["YEAR"] < 2007) & (final_tx_df["BUYER_STATE"] != "TX"),
#     (final_tx_df["YEAR"] >= 2007) & (final_tx_df["BUYER_STATE"] != "TX"),
#     (final_tx_df["YEAR"] < 2007) & (final_tx_df["BUYER_STATE"] == "TX"),
#     (final_tx_df["YEAR"] >= 2007) & (final_tx_df["BUYER_STATE"] == "TX"),
# ]
# choices = [
#     "before_policy_control",
#     "after_policy_control",
#     "before_policy_TX",
#     "after_policy_TX",
# ]

# palette = {
#     "before_policy_control": "red",
#     "after_policy_control": "red",
#     "before_policy_TX": "blue",
#     "after_policy_TX": "blue",
# }

# final_tx_df["policy_change"] = np.select(conditions, choices, default="other")
# print(final_tx_df.head())

# sns.lmplot(
#     data=final_tx_df,
#     x="YEAR",
#     y="MME",
#     hue="policy_change",
#     palette=palette,
#     hue_order=choices,
#     scatter=False,
# )
# plt.axvline(x=2007, color="r", linestyle="--")
# plt.title("Difference-in-Differences Plot Texas")
# plt.xlabel("YEAR")
# plt.ylabel("Opioids per Capita")
# plt.show()
