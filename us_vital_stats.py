import pandas as pd


data = pd.read_parquet("three_states_2.parquet", engine="pyarrow")


data.head(10)


data["BUYER_STATE"].unique()


unique_counties = data.groupby("BUYER_STATE")["BUYER_COUNTY"].unique().to_frame()


unique_counties.iloc[0][0]


data.dtypes

# Create a datetime variable and add new year column


data["TRANSACTION_DATE"] = pd.to_datetime(data["TRANSACTION_DATE"])


data["TRANSACTION_YEAR"] = data["TRANSACTION_DATE"].dt.year


data.head(10)

# ##  Death data

import os


def replace_in_files(folder_path, old_text, new_text):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(old_text, new_text)

            # Write the file out again
            with open(file_path, "w") as file:
                file.write(filedata)


# Replace 'your_folder_path' with the path of the folder containing your text files
folder_path = "/Users/udyansachdev/Downloads/US_VitalStatistics"

# Replace 'abcd' with the old text you want to replace, and 'ram' with the new text
old_text = """---"
"Dataset: Underlying Cause of Death, 1999-2017"
"Query Parameters:"
"Group By: County; Year; Drug/Alcohol Induced Cause"
"Show Totals: Disabled"
"Show Zero Values: Disabled"
"Show Suppressed: False"
"---"
"Help: See http://wonder.cdc.gov/wonder/help/ucd.html for more information."
"---"
"Suggested Citation: Centers for Disease Control and Prevention, National Center for Health Statistics. Underlying Cause of Death"
"1999-2017 on CDC WONDER Online Database, released December, 2018. Data are from the Multiple Cause of Death Files, 1999-2017, as"
"compiled from data provided by the 57 vital statistics jurisdictions through the Vital Statistics Cooperative Program. Accessed"
"at http://wonder.cdc.gov/ucd-icd10.html on Oct 1, 2019 2:59:43 PM"
"---"""
new_text = ""

replace_in_files(folder_path, old_text, new_text)


import os


def merge_text_files(folder_path, output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r") as infile:
                    outfile.write(infile.read())


# Replace 'your_folder_path' with the path of the folder containing your text files
folder_path = "/Users/udyansachdev/Downloads/US_VitalStatistics"

# Replace 'output.txt' with the desired name for the merged file
output_file = "output.txt"

merge_text_files(folder_path, output_file)


import csv
import re

# Read the contents of the text file
with open("output.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Specify the CSV file name
csv_file_name = "output.csv"

# Use a regular expression to split lines based on spaces (adjust the pattern accordingly)
pattern = re.compile(r"\s+")

# Write the contents to a CSV file
with open(csv_file_name, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write each line as a row in the CSV file
    for line in data.split("\n"):
        csv_writer.writerow(pattern.split(line.strip()))

print(f"The contents have been successfully saved in {csv_file_name}")


df = pd.read_csv(
    "output.txt", sep=r"\t", encoding="utf-8", engine="python"
).reset_index(drop=True)


df = df.loc[:57432]


colnames = list(df.columns.values)[1:]


df = df.drop("Deaths", axis=1)


df.columns = colnames


df = df[df.County != '""']
df = df[df.County != "Notes"]


# Missing value of death
df["Deaths"].value_counts()["Missing"]

# ##### Death number as 999 need to be corrected


df.to_csv("US_Vital_Stats_Deaths.csv", index=False)


