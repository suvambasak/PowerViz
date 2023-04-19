from sklearn.manifold import TSNE
import plotly.express as px

import pandas as pd


def t_sne_2d(selected_dimensions, perplexity, step):
    print(selected_dimensions)
    print(perplexity)
    print(step)

    df = pd.read_csv('dataset/HomeDHM.csv')
    columns_to_drop = df.columns[0:5].tolist() + df.columns[6:21].tolist()
    df = df.drop(columns_to_drop, axis=1)
    print(df.columns)
    num_rows = df.shape[0]
    print(num_rows)
    # 8000 is the number of data points for t-sne , change here to change the number of points
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

    tsne = TSNE(n_components=2, verbose=1, random_state=123)
    z = tsne.fit_transform(x)
    fig = px.scatter(
        z, x=0, y=1,
        color=y
    )

    return fig
    # fig.write_html("scatter_plot_2d_huge.html")
    # fig.show()
    # df2 = pd.DataFrame()
    # df2["y"] = y
    # df2["comp-1"] = z[:,0]
    # df2["comp-2"] = z[:,1]

    # sns.scatterplot(x="comp-1", y="comp-2", hue=df2.y.tolist(),
    #                 data=df2).set(title="Data T-SNE projection")
    # plt.savefig('t-sne.png')
    # # palette=sns.color_palette("hls", 3),


def t_sne_3d(selected_dimensions, perplexity, step):
    print(selected_dimensions)
    print(perplexity)
    print(step)

    df = pd.read_csv('dataset/HomeDHM.csv')
    columns_to_drop = df.columns[0:5].tolist() + df.columns[6:21].tolist()
    df = df.drop(columns_to_drop, axis=1)
    print(df.columns)
    num_rows = df.shape[0]
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
    return fig
    # fig.write_html("scatter_plot_3d_huge.html")
    # fig.show()
    # df2 = pd.DataFrame()
    # df2["y"] = y
    # df2["comp-1"] = z[:,0]
    # df2["comp-2"] = z[:,1]

    # sns.scatterplot(x="comp-1", y="comp-2", hue=df2.y.tolist(),
    #                 data=df2).set(title="Data T-SNE projection")
    # plt.savefig('t-sne.png')
    # # palette=sns.color_palette("hls", 3),
