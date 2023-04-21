import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from dataset.attributes import Attributes
from dataset.sampling import sample

attr = Attributes()


def pca_weather_plot(percentage, dim):
    df = sample(percentage)

    # Weather
    dff = df[attr.get_weather_attributes()]
    data_size = dff.shape[0]

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
            color=Attributes.temperature,
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_weather()
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
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_weather()
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
    df = sample(percentage)

    # Appliance
    dff = df[attr.get_appliance_attributes()]
    data_size = dff.shape[0]

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
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_electric()
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
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_electric()
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
    df = sample(percentage)

    # All
    dff = df[attr.all_attributes()]
    data_size = dff.shape[0]

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
            color=Attributes.temperature,
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_all()
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
            title=f"Principal Component Analysis | Size {data_size}",
            hover_data=attr.get_hover_data_for_all()
        )
        fig.update_layout(
            scene=dict(
                xaxis_title="Principle component 1",
                yaxis_title="Principle component 2",
                zaxis_title="Principle component 3"
            )
        )

    return fig
