from umap import UMAP

from dataset.attributes import Attributes
from dataset.sampling import sample
from reduction_plot import DRType, dr_plot_2d, dr_plot_3d

attr = Attributes()


def umap_weather_plot(percentage, dim, n_neighbors=15):
    df = sample(percentage)

    # Weather
    dff = df[attr.get_weather_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.temperature,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_weather(),
            DRType.UMAP
        )

    elif dim == '3D':
        umap = UMAP(n_components=3, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.temperature,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_weather(),
            DRType.UMAP
        )


def umap_electric_plot(percentage, dim, n_neighbors=15):
    df = sample(percentage)

    # Appliance
    dff = df[attr.get_appliance_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.total_energy_consumption,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_electric(),
            DRType.UMAP
        )

    if dim == '3D':
        umap = UMAP(n_components=3, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.total_energy_consumption,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_electric(),
            DRType.UMAP
        )


def umap_all_plot(percentage, dim, n_neighbors=15):
    df = sample(percentage)

    # All
    dff = df[attr.all_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        umap = UMAP(n_components=2, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.temperature,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_all(),
            DRType.UMAP
        )

    if dim == '3D':
        umap = UMAP(n_components=3, init='random',
                    random_state=0, n_neighbors=n_neighbors)
        proj = umap.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.total_energy_consumption,
            f"Uniform Manifold Approximation and Projection | Size {data_size} | n_neighbors {n_neighbors}",
            attr.get_hover_data_for_all(),
            DRType.UMAP
        )
