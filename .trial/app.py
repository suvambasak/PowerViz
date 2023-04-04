from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from data_handler import HomeData
from attributes import Attributes, build_labels

dataset = HomeData()
date_list = dataset.get_date_list()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("PowerViz", style={'textAlign': 'center'}),
        dcc.Graph(id='top-overview-plot'),
        dcc.Slider(
            min=0,
            max=len(date_list)-1,
            value=0,
            step=1,
            marks={date: date_list[date] for date in range(len(date_list))},
            id='date-slider'
        )
    ]
)


@app.callback(
    Output(component_id='top-overview-plot', component_property='figure'),
    Input(component_id='date-slider', component_property='value')
)
def update_main_figure(selected_date):
    print(selected_date)
    df = dataset.get_day_wise_mean(date_list[selected_date])

    fig = px.line(
        df,
        x="time",
        y=[
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.solar_power_generation,
            Attributes.temperature,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.pressure,
            Attributes.wind_speed
        ],
        title="Overview",
        markers=True,
        labels=build_labels()
    )
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
