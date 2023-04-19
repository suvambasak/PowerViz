import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("dataset/HomeDHM.csv", low_memory=False)


def bar_plot(day):

    df['hour_bin'] = pd.cut(df['hour'], bins=range(0, 25), labels=range(0, 24))

    # Group the data by day and hour, and calculate the sum of 'use [kW]' and 'gen [kW]' for each group.
    df_grouped = df.groupby(['day', 'hour_bin']).sum()[
        ['use [kW]', 'gen [kW]']]
    df_grouped.reset_index(inplace=True)

    fig = go.Figure()
    # Set default view to Day 1
    default_day = day
    default_data = df_grouped.loc[df_grouped['day'] == default_day]

    colors = ['#59bfd8', '#eb672f']
    items = ['use [kW]', 'gen [kW]']
    for item, color in zip(items, colors):
        fig.add_trace(go.Bar(
            x=default_data['hour_bin'], y=default_data[item], marker_color=color, name=item
        ))

    # one button for each df column
    # slice the DataFrame and apply transpose to reshape it correctly
#     buttons=[]
#     for day in df_grouped['day'].unique():
#         buttons.append(dict(method='update',
#                             label="Day " + str(day),
#                             args=[{
#                             'y': df_grouped.loc[df_grouped['day'] == day][items].T.values
#                             }])
#                       )


#     # some adjustments to the updatemenu
#     # from code by vestland
#     updatemenu=[]
#     your_menu=dict()
#     updatemenu.append(your_menu)
#     updatemenu[0]['buttons']=buttons
#     updatemenu[0]['direction']='down'
#     updatemenu[0]['showactive']=True

    fig.update_layout(
        # title="Power Usage and Generation",
        xaxis_title="Hour Bin",
        yaxis_title="Power [kW]",
        # updatemenus=updatemenu
    )

    return fig
