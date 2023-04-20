import plotly.express as px
import pandas as pd

from sklearn.preprocessing import StandardScaler
from dataset.attributes import Attributes

from sklearn.decomposition import PCA


attr = Attributes()


def pca_weather_plot(percentage, dim):

    df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
    df = df.sample(df.shape[0]*percentage//100)

    # Weather
    dff = df[attr.get_weather_attributes()]
    scaler = StandardScaler()
    scaler.fit(dff)
    scaled_data = scaler.transform(dff)

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
        pca = PCA(n_components=2)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            color=Attributes.temperature,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Principle component 1",
            yaxis_title="Principle component 2"
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter_3d(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            z=x_pca[:, 2],
            color=Attributes.temperature,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )

        fig.update_layout(
            scene=dict(
                xaxis_title="Principle component 1",
                yaxis_title="Principle component 2",
                zaxis_title="Principle component 3"
            )
        )

    return fig


def pca_electric_plot(percentage, dim):
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

    scaler = StandardScaler()
    scaler.fit(dff)
    scaled_data = scaler.transform(dff)

    if dim == '2D':
        pca = PCA(n_components=2)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            color=Attributes.total_energy_consumption,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Principle component 1",
            yaxis_title="Principle component 2"
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter_3d(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            z=x_pca[:, 2],
            color=Attributes.total_energy_consumption,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Principle component 1",
                yaxis_title="Principle component 2",
                zaxis_title="Principle component 3"
            )
        )

    return fig


def pca_all_plot(percentage, dim):
    df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
    df = df.sample(df.shape[0]*percentage//100)

    # All
    dff = df[attr.all_attributes()]
    scaler = StandardScaler()
    scaler.fit(dff)
    scaled_data = scaler.transform(dff)

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
        pca = PCA(n_components=2)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            color=Attributes.temperature,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            xaxis_title="Principle component 1",
            yaxis_title="Principle component 2"
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        fig = px.scatter_3d(
            df,
            x=x_pca[:, 0],
            y=x_pca[:, 1],
            z=x_pca[:, 2],
            color=Attributes.total_energy_consumption,
            title="Principal component analysis",
            hover_data=get_hover_data()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Principle component 1",
                yaxis_title="Principle component 2",
                zaxis_title="Principle component 3"
            )
        )

    return fig
