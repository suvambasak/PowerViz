import plotly.graph_objects as go


def plot_rolling_average(df, window_size, column_name):

    # Group the data by day and get the sum of the column specified by the user
    df_grouped = df.groupby('day').agg({column_name: 'sum'})
    df_grouped[column_name] = df_grouped[column_name].div(1440)
    # print(df_grouped)

    # Obtain the rolling mean of last 'window_size' days and reindex the database accordingly
    rolling_mean = df_grouped.rolling(window_size, min_periods=1).mean()
    rolling_mean.reset_index(inplace=True)
    # print(rolling_mean)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=rolling_mean['day'],
            y=rolling_mean[column_name],
            mode='lines',
            name='Rolling mean value'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_grouped.index,
            y=df_grouped[column_name],
            mode='lines',
            name=f'Actual {column_name}'
        )
    )

    fig.update_layout(
        title="Prediction from past three days",
        xaxis_title='Day',
        yaxis_title=column_name
    )

    return fig
