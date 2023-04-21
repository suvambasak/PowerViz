import pandas as pd
import plotly.graph_objects as go


def plot_rolling_average(window_size, column_name):
    df = pd.read_csv("dataset/HomeDHM.csv", low_memory=False)

    # Group the data by day and get the sum of the column specified by the user
    df_grouped = df.groupby('day').agg({column_name: 'sum'})

    # Obtain the rolling mean of last 'window_size' days and reindex the database accordingly
    rolling_mean = df_grouped.rolling(window_size, min_periods=1).mean()
    rolling_mean.reset_index(inplace=True)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=rolling_mean['day'],
            y=rolling_mean['use [kW]'],
            mode='lines',
            name='Rolling mean value (W)'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_grouped.index,
            y=df_grouped[column_name],
            mode='lines',
            name=f'Actual use (W)'
        )
    )
    fig.update_layout(
        title="Power usage prediction from past data",
        xaxis_title='Day',
        yaxis_title='Power use (W)'
    )

    return fig
    # fig.show()


# plot_rolling_average(4, 'use [kW]')
