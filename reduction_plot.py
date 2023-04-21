import plotly.express as px


class DRType:
    PCA = 'PCA'
    UMAP = 'UMAP'
    TSNE = 't-SNE'


def dr_plot_2d(
        df,
        x,
        y,
        color_attr,
        title,
        hover_data,
        method
):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color_attr,
        title=title,
        hover_data=hover_data
    )

    if method == DRType.PCA:
        fig.update_layout(
            xaxis_title="Principle component 1",
            yaxis_title="Principle component 2"
        )

    elif method == DRType.TSNE or method == DRType.UMAP:
        fig.update_layout(
            xaxis_title="Dimension 1",
            yaxis_title="Dimension 2",
        )

    return fig


def dr_plot_3d(
        df,
        x,
        y,
        z,
        color_attr,
        title,
        hover_data,
        method
):
    fig = px.scatter_3d(
        df,
        x=x,
        y=y,
        z=z,
        color=color_attr,
        title=title,
        hover_data=hover_data
    )

    if method == DRType.PCA:
        fig.update_layout(
            scene=dict(
                xaxis_title="Principle component 1",
                yaxis_title="Principle component 2",
                zaxis_title="Principle component 3"
            )
        )

    elif method == DRType.TSNE or method == DRType.UMAP:
        fig.update_layout(
            scene=dict(
                xaxis_title="Dimension 1",
                yaxis_title="Dimension 2",
                zaxis_title="Dimension 3"
            )
        )

    return fig
