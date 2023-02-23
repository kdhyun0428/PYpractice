import pandas as pd
import matplotlib.pyplot as plt

# Read the data from an online source
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
data = pd.read_csv(url)

# Filter out the countries with the highest number of deaths
top_countries = data.groupby('location')['total_deaths'].max().sort_values(ascending=False).head(10)
data = data[data['location'].isin(top_countries.index)]

# Calculate the mortality rate per country
data['mortality_rate'] = data['total_deaths'] / data['total_cases']

# Plot a bar chart of the mortality rate per country
plt.bar(data['location'], data['mortality_rate'])
plt.title('Global COVID-19 Mortality Rate')
plt.xlabel('Country')
plt.ylabel('Mortality Rate')
plt.xticks(rotation=45)
plt.show()
