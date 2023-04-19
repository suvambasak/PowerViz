from sklearn.manifold import TSNE
import plotly.express as px

import pandas as pd
from sklearn.manifold import TSNE
# import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('HomeDHM.csv')
columns_to_drop = df.columns[0:5].tolist() + df.columns[6:21].tolist()
df = df.drop(columns_to_drop, axis=1)
print(df.columns)
num_rows =  df.shape[0]
print(num_rows)
sel = num_rows//8000
df = df.iloc[::sel, :]
# df = df.drop(columns=['day', 'hour', 'minute', ''])
x = df.drop(columns=['House overall [kW]'])
y = df['House overall [kW]']
for col in x.select_dtypes(exclude=['int', 'float']).columns:
    x[col] = pd.Categorical(x[col], categories=x[col].unique()).codes
    # print(df[col].dtype)
# print(x.dtypes)


# x = x[:60]
# y = y[:60]

tsne = TSNE(n_components=3, verbose=1, random_state=123)
z = tsne.fit_transform(x,)
fig = px.scatter_3d(
    z, x=0, y=1, z=2,
    color=y, labels={'color': 'species'}
)
fig.update_traces(marker_size=3)
fig.write_html("scatter_plot_3d_huge.html")
fig.show()
# df2 = pd.DataFrame()
# df2["y"] = y
# df2["comp-1"] = z[:,0]
# df2["comp-2"] = z[:,1]

# sns.scatterplot(x="comp-1", y="comp-2", hue=df2.y.tolist(),
#                 data=df2).set(title="Data T-SNE projection") 
# plt.savefig('t-sne.png')
# # palette=sns.color_palette("hls", 3),