import plotly.express as px
import pandas as pd
from dataset.attributes import Attributes


ip = ['day', 'hour', 'minute', 'use [kW]', 'gen [kW]', 'Dishwasher [kW]', 'Furnace 2 [kW]', 'Fridge [kW]', 'Home office [kW]', 'Garage door [kW]', 'Wine cellar [kW]', 'Furnace 1 [kW]', 'Kitchen 14 [kW]', 'Kitchen 38 [kW]', 'Well [kW]', 'Barn [kW]', 'Living room [kW]',
      'Solar [kW]', 'temperature', 'icon', 'humidity', 'visibility', 'summary', 'apparentTemperature', 'Microwave [kW]', 'cloudCover', 'windSpeed', 'pressure', 'precipIntensity', 'precipProbability', 'windBearing', 'dewPoint', 'Kitchen 12 [kW]', 'House overall [kW]']

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
dff = df[(df['day'] >= int(1)) &
         (df['day'] <= int(1))]
# print(dff.corr())


# print(dff[Attributes.barn].corr(dff[Attributes.fridge]))

# Choose a column to sort by correlation
col = Attributes.apparent_temperature

# Calculate correlation between all columns and the chosen column
corr = dff[[Attributes.barn, Attributes.furnace_1,
            Attributes.furnace_1]].corrwith(dff[col])

# Sort columns based on correlation with the chosen column
sorted_cols = corr.abs().sort_values(ascending=False).index
print(sorted_cols)
# dff_sorted = dff[sorted_cols]
# print(dff_sorted)
