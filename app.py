from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from dataset.attributes import Attributes
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([


    html.Div(
        [
            html.H1('PowerViz')
        ], className='text-center'
    ),


    html.Hr(),



    # Overview dataset
    html.Div([
        html.H4('Dataset Overview'),

        # Inputs
        html.Div([
            # Start Day
            html.Div([
                html.Label('Start Day'),
                dcc.Dropdown(
                    df['day'].unique(),
                    '1',
                    id='start-day'
                ),
            ], style={'width': '48%', 'display': 'inline-block'}, className='form-group'),

            # End Day
            html.Div([
                html.Label('End Day'),
                dcc.Dropdown(
                    df['day'].unique(),
                    '1',
                    id='end-day'
                ),
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}, className='form-group'),

            # Dimention
            html.Div([
                html.Label('Select dimensions'),
                dcc.Dropdown([
                    Attributes.day,
                    Attributes.hour,
                    Attributes.minute,
                    Attributes.total_energy_consumption,
                    Attributes.total_energy_generated,
                    Attributes.overall_house_energy_consumption,
                    Attributes.dishwasher,
                    Attributes.furnace_1,
                    Attributes.furnace_2,
                    Attributes.home_office,
                    Attributes.fridge,
                    Attributes.wine_cellar,
                    Attributes.garage_door,
                    Attributes.kitchen_1,
                    Attributes.kitchen_2,
                    Attributes.kitchen_3,
                    Attributes.barn,
                    Attributes.well,
                    Attributes.microwave,
                    Attributes.living_room,
                    Attributes.solar_power_generation,
                    Attributes.temperature,
                    Attributes.overall_weather_condition,
                    Attributes.humidity,
                    Attributes.visibility,
                    Attributes.summarise_weather,
                    Attributes.apparent_temperature,
                    Attributes.pressure,
                    Attributes.wind_speed,
                    Attributes.cloud_cover,
                    Attributes.wind_bearing,
                    Attributes.precipitation_intensity,
                    Attributes.dew_point,
                    Attributes.precipitation_probability],
                    [Attributes.day, Attributes.hour],
                    multi=True,
                    id='overview-dimension-list'),
            ], className='form-group'),
        ]
        ),
        dcc.Graph(id='overview-parallel-coordinates'),
        dcc.Graph(id='overview-correlation-coordinates'),

    ], className='container'),

    html.Hr(),


], className='container')


@app.callback(
    Output(component_id='overview-parallel-coordinates',
           component_property='figure'),
    Output(component_id='overview-correlation-coordinates',
           component_property='figure'),
    Input(component_id='start-day', component_property='value'),
    Input(component_id='end-day', component_property='value'),
    Input(component_id='overview-dimension-list', component_property='value'),
)
def update_output_div(start_day, end_day, selected_dimensions):

    dff = df[(df['day'] >= int(start_day)) &
             (df['day'] <= int(end_day))]

    fig = px.parallel_coordinates(
        dff,
        color=Attributes.minute,
        dimensions=selected_dimensions,
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=2)

    fig1 = px.imshow(dff[selected_dimensions].corr(), text_auto=True)

    return [fig, fig1]


if __name__ == '__main__':
    app.run_server(debug=True)
