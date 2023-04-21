import pandas as pd

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)


def sample_points(percentage):
    dff = df.sample(df.shape[0]*percentage//100)
    return dff.shape[0]
