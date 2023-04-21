from sklearn.manifold import TSNE

from dataset.attributes import Attributes
from dataset.sampling import sample
from reduction_plot import DRType, dr_plot_2d, dr_plot_3d

attr = Attributes()


def t_sne_weather_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # Weather
    dff = df[attr.get_weather_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.temperature,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_weather(),
            DRType.TSNE
        )

    elif dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.temperature,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_weather(),
            DRType.TSNE
        )


def t_sne_electric_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # Appliance
    dff = df[attr.get_appliance_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.total_energy_consumption,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_electric(),
            DRType.TSNE
        )

    if dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.total_energy_consumption,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_electric(),
            DRType.TSNE
        )


def t_sne_all_plot(percentage, dim, perplexity=30):
    df = sample(percentage)

    # All
    dff = df[attr.all_attributes()]
    data_size = dff.shape[0]

    if dim == '2D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_2d(
            df,
            proj[:, 0],
            proj[:, 1],
            Attributes.temperature,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_all(),
            DRType.TSNE
        )

    if dim == '3D':
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        proj = tsne.fit_transform(dff)

        return dr_plot_3d(
            df,
            proj[:, 0],
            proj[:, 1],
            proj[:, 2],
            Attributes.total_energy_consumption,
            f"t-Distributed Stochastic Neighbor Embedding | Size {data_size} | Perplexity {perplexity}",
            attr.get_hover_data_for_all(),
            DRType.TSNE
        )
