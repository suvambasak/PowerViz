import pandas as pd
from attributes import Attributes


class HomeData:
    _CSV_FILE = 'dataset/Home.csv'

    def __init__(self) -> None:
        self.df = pd.read_csv(self._CSV_FILE, low_memory=False)

    def get_date_list(self):
        return self.df.date.unique()

    def get_day_wise_mean(self, date):
        dff = self.df.loc[
            (self.df[Attributes.date] == date)
        ].sort_values(Attributes.time)

        hour_wise_mean = []

        for hour in range(24):
            start_time = f"{hour}:00:00"
            end_time = f"{hour}:59:59"

            hour_data = dff.loc[
                (dff[Attributes.time] >= start_time) &
                (dff[Attributes.time] <= end_time)
            ].fillna(0)

            if hour_data.empty:
                continue

            hour_mean = hour_data.mean().to_dict()
            hour_mean["time"] = start_time
            hour_wise_mean.append(hour_mean)

        # print(pd.DataFrame.from_dict(hour_wise_mean))
        return pd.DataFrame.from_dict(hour_wise_mean)

    def get_date_wise_mean(self):
        dates = self.df.date.unique()

        dff = self.df.groupby(self.df.date).mean()
        dff[Attributes.date] = dates

        return dff


if __name__ == '__main__':
    dataset = HomeData()
    # dataset.get_date_wise_mean()
    date_list = dataset.get_date_list()
    # print(date_list)
    # print(date_list[6])
    dataset.get_day_wise_mean(date_list[6])
