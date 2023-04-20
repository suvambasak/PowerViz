from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from dataset.attributes import Attributes
import pandas as pd
import dash_bootstrap_components as dbc
from reduction import t_sne_2d, t_sne_3d
from bar import bar_plot
from pie import pie_chart

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
attr = Attributes()


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
                dcc.Dropdown(attr.get_attr_list(),
                             [Attributes.day, Attributes.hour],
                             multi=True,
                             id='overview-dimension-list'),
            ], className='form-group'),

            # Correlation dimention
            html.Div([
                html.Label('Correlation dimensions'),
                dcc.Dropdown(
                    id='correlation-dimension',
                    options=attr.get_attr_list()
                ),
            ], className='form-group'),
            html.Hr(),
        ]
        ),

        html.Div([
            html.H6(['Parallel coordinates view'], className='text-center'),
            dcc.Graph(id='overview-parallel-coordinates'),
            html.H6(['Correlation 2D view'], className='text-center'),
            dcc.Graph(id='overview-correlation-coordinates'),
        ]),

    ], className='container'),

    html.Hr(),
    # Bar and Pie side by side

    html.Div([
        html.H4('Power'),

        html.Div([
            # Gen vs Usage
            html.Div([
                html.Label('For day'),
                dcc.Dropdown(
                    df['day'].unique(),
                    value=1,
                    id='power-day'
                ),
                dcc.Graph(id='bar-graph'),
            ], style={'width': '48%', 'display': 'inline-block'}),

            # Home appliances
            html.Div([
                html.Label('Select appliances'),
                dcc.Dropdown(attr.get_appliance_list(),
                             [Attributes.home_office, Attributes.living_room],
                             multi=True,
                             id='appliances-pie-list'),
                dcc.Graph(id='pie-graph'),
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        ], className='container'),


    ], className='container'),

    html.Hr(),

    # t-SNE
    html.Div([
        html.H4('Dimensionality reduction'),
        html.Div([
            html.Div([
                html.Div([
                    html.Label('Perplexity'),
                    dcc.Slider(0, 20, 5,
                               value=10,
                               id='perplexity-slider'
                               ),

                ], className='col-6'),
                html.Div([
                    html.Label('Plot'),
                    dcc.RadioItems(
                        ['2D', '3D'],
                        '2D',
                        id='tsne-plot',
                        inline=True
                    ),
                ], className='col'),
                html.Div([
                    html.Label(''),
                    html.Button(id='t-sne-button', n_clicks=0,
                                children='Update', className='btn btn-success'),
                ], className='col'),


            ], className='row')

        ], className='container'),

        dcc.Graph(id='t-sne'),
    ], className='container'),


    html.Hr(),

], className='container')


@app.callback(
    Output(component_id='pie-graph',
           component_property='figure'),
    Input(component_id='power-day', component_property='value'),
    Input(component_id='appliances-pie-list', component_property='value'),
)
def update_pie_chart(day, appliances):
    return pie_chart(day, appliances)


@app.callback(
    Output(component_id='bar-graph',
           component_property='figure'),
    Input(component_id='power-day', component_property='value'),
)
def update_bar_chart(day):
    print('DAY:', day)
    return bar_plot(day)


@app.callback(
    Output(component_id='t-sne',
           component_property='figure'),
    Input('t-sne-button', 'n_clicks'),
    State(component_id='overview-dimension-list', component_property='value'),
    State(component_id='perplexity-slider', component_property='value'),
    State(component_id='tsne-plot', component_property='value'),
)
def update_dimensionality_reduction(clicks, selected_dimensions, perplexity, plot_dim):

    if plot_dim == '2D':
        return t_sne_2d(selected_dimensions, perplexity, 0)
    if plot_dim == '3D':
        return t_sne_3d(selected_dimensions, perplexity, 0)


@app.callback(
    Output(component_id='overview-parallel-coordinates',
           component_property='figure'),
    Output(component_id='overview-correlation-coordinates',
           component_property='figure'),
    Input(component_id='start-day', component_property='value'),
    Input(component_id='end-day', component_property='value'),
    Input(component_id='overview-dimension-list', component_property='value'),
    Input(component_id='correlation-dimension', component_property='value'),
)
def parallel_correlation(start_day, end_day, selected_dimensions, selected_correlation):

    dff = df[(df['day'] >= int(start_day)) &
             (df['day'] <= int(end_day))]

    if selected_correlation:
        corr = dff.corrwith(dff[selected_correlation])
        sorted_cols = corr.abs().sort_values(ascending=False).index

        ordered_dimentions = []
        for dim in sorted_cols:
            if dim in selected_dimensions:
                ordered_dimentions.append(dim)

    else:
        ordered_dimentions = selected_dimensions

    parallel_coordinates_fig = px.parallel_coordinates(
        dff,
        color=Attributes.minute,
        dimensions=ordered_dimentions,
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=2
    )

    correlation_grid_fig = px.imshow(
        dff[ordered_dimentions].corr(), text_auto=True)

    return [parallel_coordinates_fig, correlation_grid_fig]


if __name__ == '__main__':
    app.run_server(debug=True)
