import pandas as pd
from dataset.attributes import Attributes
from umap import UMAP
import plotly.express as px


attr = Attributes()


def umap_weather_plot(percentage, dim):
    df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
    df = df.sample(df.shape[0]*percentage//100)

    # Weather
    dff = df[attr.get_weather_attributes()]

    def get_hover_data():
        return [
            Attributes.id,
            Attributes.overall_weather_condition,
            Attributes.summarise_weather,
            Attributes.cloud_cover,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.pressure,
        ]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.temperature,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    elif dim == '3D':
        umap = UMAP(n_components=3, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.temperature,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )

        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig


def umap_electric_plot(percentage, dim):
    df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
    df = df.sample(df.shape[0]*percentage//100)

    # Appliance
    dff = df[attr.get_appliance_attributes()]

    def get_hover_data():
        return [
            Attributes.id,
            Attributes.dishwasher,
            Attributes.living_room,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.microwave,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.well,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn
        ]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.total_energy_consumption,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    if dim == '3D':
        umap = UMAP(n_components=3, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.total_energy_consumption,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig


def umap_all_plot(percentage, dim):
    df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
    df = df.sample(df.shape[0]*percentage//100)

    # All
    dff = df[attr.all_attributes()]

    def get_hover_data():
        return [
            Attributes.id,
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.humidity,
            Attributes.summarise_weather
        ]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            color=Attributes.temperature,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2"
        )

    if dim == '3D':
        umap = UMAP(n_components=3, init='random', random_state=0)
        proj = umap.fit_transform(dff)

        fig = px.scatter_3d(
            df,
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            color=Attributes.total_energy_consumption,
            title="Uniform Manifold Approximation and Projection",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig
