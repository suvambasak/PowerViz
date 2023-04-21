import pandas as pd

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)


def sample(percentage):
    return df.sample(df.shape[0]*percentage//100)


def sample_points(percentage):
    dff = sample(percentage)
    return dff.shape[0]
