from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from dataset.attributes import Attributes
from dataset.sampling import sample
from reduction_plot import DRType, dr_plot_2d, dr_plot_3d

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

        return dr_plot_2d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            Attributes.temperature,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_weather(),
            DRType.PCA
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        return dr_plot_3d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            x_pca[:, 2],
            Attributes.temperature,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_weather(),
            DRType.PCA
        )


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

        return dr_plot_2d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            Attributes.total_energy_consumption,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_electric(),
            DRType.PCA
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        return dr_plot_3d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            x_pca[:, 2],
            Attributes.total_energy_consumption,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_electric(),
            DRType.PCA
        )


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

        return dr_plot_2d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            Attributes.temperature,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_all(),
            DRType.PCA
        )

    elif dim == '3D':
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        x_pca = pca.transform(scaled_data)

        return dr_plot_3d(
            df,
            x_pca[:, 0],
            x_pca[:, 1],
            x_pca[:, 2],
            Attributes.total_energy_consumption,
            f"Principal Component Analysis | Size {data_size}",
            attr.get_hover_data_for_all(),
            DRType.PCA
        )
