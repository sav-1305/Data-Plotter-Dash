from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import dash_bootstrap_components as dbc

csv_file_path = 'SampleData.csv'
df = pd.read_csv(csv_file_path)

app = Dash(__name__, external_stylesheets=[dbc.themes.MATERIA])

data_points_to_plot = 100

current_index = 0

@app.callback(
    [Output('velocity-plot', 'figure'),
     Output('altitude-plot', 'figure'),
     Output('pressure-plot', 'figure'),
     Output('latest-values', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_live_plots_and_values(n):
    global df, current_index

    df = pd.read_csv(csv_file_path)

    start_index = current_index
    end_index = current_index + data_points_to_plot

    if end_index > len(df):
        end_index = data_points_to_plot
        current_index = 0

    subset_df = df.iloc[start_index:end_index]

    current_index = end_index

    velocity_fig = px.line(subset_df, x='time', y='velocity', markers=True, height=350, title="Velocity")
    altitude_fig = px.line(subset_df, x='time', y='altitude', markers=True, height=350, title="Altitude")
    pressure_fig = px.line(subset_df, x='time', y='pressure', markers=True, height=350, title="Pressure")

    latest_values = [
        html.Div(f"Velocity: {subset_df['velocity'].iloc[-1]:.2f} m/s"),
        html.Div(f"Altitude: {subset_df['altitude'].iloc[-1]:.2f} m"),
        html.Div(f"Pressure: {subset_df['pressure'].iloc[-1]:.2f} KPa")
    ]

    return velocity_fig, altitude_fig, pressure_fig, latest_values

app.layout = html.Div([
    html.H1("Live Data Plotter", style={'text-align': 'center'}),

    html.Div([
        html.H4("Latest Values", style={'text-align': 'center'}),
        html.Div(id='latest-values', style={'font-size': '18px', 'text-align': 'center', 'margin': '20px', 'padding': '10px', 'box-shadow': '2px 2px 4px rgb(67, 63, 77)'})
    ], style={'width': '20%', 'margin': 'auto', 'margin-top': '20px'}),

    html.Div([
        dcc.Graph(id='velocity-plot'),
        dcc.Graph(id='altitude-plot'),
        dcc.Graph(id='pressure-plot'),
    ], style={'width': '80%', 'margin': 'auto'}),
    
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
