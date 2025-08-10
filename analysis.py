"""Analyzes and visualizes crash data from flight.csv"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

URL = "flight.csv"

# Load the data
flight_df = pd.read_csv(URL)

# Remove bad data
flight_df.dropna(inplace=True)
flight_df.drop_duplicates(inplace=True)

# Converting the date to a usable format, and drop rows where the date cannot be used
flight_df["acc.date"] = pd.to_datetime(flight_df["acc.date"], errors='coerce')
flight_df.dropna(subset=["acc.date"], inplace=True)

# Extract the year from each row's date
flight_df["Year"] = flight_df["acc.date"].dt.year

# Find the number of crashes per year
crashes_per_year = flight_df["Year"].value_counts().sort_index()

# Create the visualization
plt.figure(figsize=(14, 8))
sns.lineplot(x=crashes_per_year.index, y=crashes_per_year.values, marker='o')
plt.title("Air Crashes Per Year", fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Crashes')
plt.grid(True)
plt.show()
