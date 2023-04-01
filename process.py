import datetime
import pandas as pd
import sys

df = pd.read_csv('dataset/HomeC.csv', low_memory=False)


def split_unix_time(df):
    def get_data_time(unix_time):
        sys.stdout.write(f'\rProcessing ({unix_time})        ')

        date, time = datetime.datetime.fromtimestamp(
            int(unix_time)
        ).strftime('%Y-%m-%d %H:%M:%S').split()

        return pd.Series(
            (date, time),
            index=['date', 'time']
        )

    date_time = df.time.apply(get_data_time)
    print()

    df.drop(['time',], axis=1)
    df[date_time.columns] = date_time
    return df


df = split_unix_time(df)

columns = ['date', 'time', 'use [kW]', 'gen [kW]', 'House overall [kW]', 'Dishwasher [kW]',
           'Furnace 1 [kW]', 'Furnace 2 [kW]', 'Home office [kW]', 'Fridge [kW]',
           'Wine cellar [kW]', 'Garage door [kW]', 'Kitchen 12 [kW]',
           'Kitchen 14 [kW]', 'Kitchen 38 [kW]', 'Barn [kW]', 'Well [kW]',
           'Microwave [kW]', 'Living room [kW]', 'Solar [kW]', 'temperature',
           'icon', 'humidity', 'visibility', 'summary', 'apparentTemperature',
           'pressure', 'windSpeed', 'cloudCover', 'windBearing', 'precipIntensity',
           'dewPoint', 'precipProbability']

df.to_csv('dataset/Home.csv', index=False, columns=columns)
