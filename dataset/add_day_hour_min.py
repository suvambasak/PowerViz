import sys

import pandas as pd

df = pd.read_csv('HomeC.csv', low_memory=False)

df = df.drop(['time'], axis=1)


id = []
count = 0
minutes = []
days = []
days_count = 1
minutes_count = 1
for row in range(len(df.index)):
    count += 1
    id.append(count)

    sys.stdout.write(f'\r ({row}/{len(df.index)})     ')

    minutes.append(1441-minutes_count)
    days.append(days_count)
    minutes_count += 1

    if minutes_count == 1441:
        minutes_count = 1
        days_count += 1

sys.stdout.write(f'\r Complete.     ')


sys.stdout.write(f'\r Adding columns.     ')
df['ID'] = id
df['minute'] = minutes
df['day'] = days
df['hour'] = df['minute'].div(60).round(2)


columns = ['ID', 'day', 'hour', 'minute', 'use [kW]', 'gen [kW]', 'House overall [kW]', 'Dishwasher [kW]',
           'Furnace 1 [kW]', 'Furnace 2 [kW]', 'Home office [kW]', 'Fridge [kW]',
           'Wine cellar [kW]', 'Garage door [kW]', 'Kitchen 12 [kW]',
           'Kitchen 14 [kW]', 'Kitchen 38 [kW]', 'Barn [kW]', 'Well [kW]',
           'Microwave [kW]', 'Living room [kW]', 'Solar [kW]', 'temperature',
           'icon', 'humidity', 'visibility', 'summary', 'apparentTemperature',
           'pressure', 'windSpeed', 'cloudCover', 'windBearing', 'precipIntensity',
           'dewPoint', 'precipProbability']

sys.stdout.write(f'\r Writing CSV       ')
df.to_csv('HomeDHMI.csv', index=False, columns=columns)
