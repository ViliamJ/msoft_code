import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from Core.logic import plotting_logic
from Core.dash_apps.app import app

available_indicators = ["Zoo", "Jakub", "Údržba"]

layout = html.Div([

    html.Div([

        dcc.Dropdown(
            id='crossfilter-profit-component',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value='Zoo')
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block', 'padding': '10px 5px'}),


    html.Div(children=[
        html.Div([
            dcc.Graph(figure=plotting_logic.total_plot())
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20', 'float': 'left'}),

        html.Div([
            dcc.Graph(id='output-profit-component')],
            style={'display': 'inline-block', 'width': '49%', 'float': 'right'})
    ])

])



@app.callback(
    Output('output-profit-component', 'figure'),
    Input('crossfilter-profit-component', 'value')
)
def update_output(value):
    fig = plotting_logic.component_values(value)
    return fig

