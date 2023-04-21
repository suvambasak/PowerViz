from dataset.sampling import sample
from dataset.attributes import Attributes
from sklearn.manifold import TSNE
import plotly.express as px


attr = Attributes()


def t_sne_weather_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # Weather
    dff = df[attr.get_weather_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.temperature,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_weather()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    elif dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.temperature,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_weather()
        )

        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig


def t_sne_electric_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # Appliance
    dff = df[attr.get_appliance_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.total_energy_consumption,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_electric()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    if dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.total_energy_consumption,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_electric()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig


def t_sne_all_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # All
    dff = df[attr.all_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.temperature,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_all()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    if dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.total_energy_consumption,
            title=f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            hover_data=attr.get_hover_data_for_all()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig
