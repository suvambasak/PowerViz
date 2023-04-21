import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, State, dcc, html

from bar import bar_plot
from dataset.attributes import Attributes
from dataset.sampling import sample_points
from pca import pca_all_plot, pca_electric_plot, pca_weather_plot
from pie import pie_chart
from t_sne import t_sne_all_plot, t_sne_electric_plot, t_sne_weather_plot
from u_map import umap_all_plot, umap_electric_plot, umap_weather_plot

df = pd.read_csv('dataset/HomeDHM.csv', low_memory=False)
attr = Attributes()


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([


    html.Div(
        [
            html.H1('PowerViz')
        ], className='text-center', style={'backgroundColor': 'black', 'color': 'white', 'padding': '7px', 'width': '100%', 'margin': '0'}
    ),
    html.Br(),


    # Overview dataset
    html.Div([
        html.Link(
            rel='stylesheet',
            href='/assets/style.css'
        ),
        html.H4('Dataset Overview', className='text-center'),

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
                dcc.Dropdown(attr.get_numeric_attributes(),
                             [Attributes.day, Attributes.hour],
                             multi=True,
                             id='overview-dimension-list'),
            ], className='form-group'),

            html.Hr(),

            # Correlation dimention
            html.Div([
                html.Label('Correlation dimensions'),
                dcc.Dropdown(
                    id='correlation-dimension',
                    options=attr.get_numeric_attributes()
                ),
            ], className='form-group'),
            html.Hr(),
        ]
        ),

        html.Div([
            html.H6(['Parallel coordinates view'], className='text-center'),
            dcc.Graph(id='overview-parallel-coordinates'),
            html.Hr(),
            html.H6(['Correlation 2D view'], className='text-center'),
            dcc.Graph(id='overview-correlation-coordinates'),
        ]),

    ], className='container'),

    html.Hr(),
    # Bar and Pie side by side

    html.Div([
        html.H4('Power and usage', className='text-center'),
        html.Br(),

        html.Div([
            # Gen vs Usage
            html.Div([
                html.Label('For day'),
                dcc.Dropdown(
                    df['day'].unique(),
                    value=1,
                    id='power-day'
                ),
                html.Hr(),
                dcc.Graph(id='bar-graph'),
            ], style={'width': '48%', 'display': 'inline-block'}),

            # Home appliances
            html.Div([
                html.Label('Select appliances'),
                dcc.Dropdown(attr.get_appliance_attributes(),
                             [Attributes.home_office, Attributes.living_room],
                             multi=True,
                             id='appliances-pie-list'),

                html.Hr(),
                dcc.Graph(id='pie-graph'),
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        ], className='container'),


    ], className='container'),

    html.Hr(),

    # t-SNE
    html.Div([
        html.H4('Dimensionality reduction', className='text-center'),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                    html.Label('Sample (%)'),
                    dcc.Slider(0, 100, 5,
                               value=30,
                               id='sample-slider'
                               ),
                    html.Label('neighbour', id='neighbour-label'),
                    dcc.Slider(min=0,
                               max=100,
                               step=5,
                               value=0,
                               id='neighbour-slider'
                               ),

                ], className='col-6'),
                html.Div([
                    html.Label('Method'),
                    dcc.RadioItems(
                        ['PCA', 'UMAP', 't-SNE'],
                        'PCA',
                        id='dim-method',
                    ),
                ], className='col'),
                html.Div([
                    html.Label('Plot type'),
                    dcc.RadioItems(
                        ['2D', '3D'],
                        '2D',
                        id='tsne-plot',
                    ),
                ], className='col'),
                html.Div([
                    html.Label('Plot with'),
                    dcc.RadioItems(
                        ['Weather', 'Power usage', 'All'],
                        'Weather',
                        id='tsne-plot-with',
                    ),
                ], className='col'),

                html.Div([
                    html.Label(id='datasize-info'),
                    html.Button(id='t-sne-button', n_clicks=0,
                                children='Reduce', className='btn btn-primary'),
                ], className='col'),


            ], className='row')

        ], className='container'),
        html.Hr(),

        dcc.Graph(id='t-sne', style={'height': '800px'}),
    ]),


    html.Hr(),

])


@app.callback(
    Output(component_id='datasize-info', component_property='children'),
    Input(component_id='sample-slider', component_property='value'),
    Input(component_id='neighbour-slider', component_property='value'),
    State(component_id='dim-method', component_property='value'),
)
def show_datasize_info(sample, neighbour_size, method):
    if sample <= 0:
        sample = 1
    current_sample_points = sample_points(sample)

    if method == 'PCA':
        return f'Sample: {current_sample_points}'

    elif method == 'UMAP':
        return f'Sample: {current_sample_points} Neighbors: {neighbour_size}'

    elif 't-SNE':
        return f'Sample: {current_sample_points} Perplexity: {neighbour_size}'


@app.callback(
    Output(component_id='t-sne-button', component_property='children'),
    Input(component_id='dim-method', component_property='value'),
)
def update_text_on_method_change(method):
    return f'Reduce with {method}'


@app.callback(
    Output(component_id='neighbour-label', component_property='children'),
    Output(component_id='neighbour-slider', component_property='value'),
    Output(component_id='neighbour-slider', component_property='max'),
    Output(component_id='neighbour-slider', component_property='step'),
    Input(component_id='dim-method', component_property='value'),
    Input(component_id='sample-slider', component_property='value'),
)
def update_neighbour_slider(method, sample):
    if sample <= 0:
        sample = 1

    current_sample_points = sample_points(sample)
    step_size = current_sample_points//20

    if method == 'PCA':
        return [f'{method}: Disabled', 0, current_sample_points, step_size]
    elif method == 'UMAP':
        return [f'{method}: n Neighbors', 15, current_sample_points, step_size]
    elif 't-SNE':
        return [f'{method}: Perplexity', 30, current_sample_points, step_size]


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
    State(component_id='sample-slider', component_property='value'),
    State(component_id='tsne-plot', component_property='value'),
    State(component_id='tsne-plot-with', component_property='value'),
    State(component_id='dim-method', component_property='value'),
    State(component_id='neighbour-slider', component_property='value'),
)
def update_dimensionality_reduction(clicks, sample, plot_dim, plot_with, method, neighbour):
    print('update_dimensionality_reduction',
          clicks, sample, plot_dim, plot_with, method, neighbour)

    if sample <= 0:
        sample = 1

    if plot_with == 'Weather':
        if method == 'PCA':
            return pca_weather_plot(sample, plot_dim)
        elif method == 'UMAP':
            return umap_weather_plot(sample, plot_dim, n_neighbors=neighbour)
        elif method == 't-SNE':
            return t_sne_weather_plot(sample, plot_dim, perplexity=neighbour)

    if plot_with == 'Power usage':
        if method == 'PCA':
            return pca_electric_plot(sample, plot_dim)
        elif method == 'UMAP':
            return umap_electric_plot(sample, plot_dim, n_neighbors=neighbour)
        elif method == 't-SNE':
            return t_sne_electric_plot(sample, plot_dim, perplexity=neighbour)

    if plot_with == 'All':
        if method == 'PCA':
            return pca_all_plot(sample, plot_dim)
        elif method == 'UMAP':
            return umap_all_plot(sample, plot_dim, n_neighbors=neighbour)
        elif method == 't-SNE':
            return t_sne_all_plot(sample, plot_dim, perplexity=neighbour)


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
    dff = dff.drop(['icon', 'summary', 'cloudCover'], axis=1)

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
    # app.run_server(host='0.0.0.0', debug=False)
