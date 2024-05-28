# Data-Plotter-Dash
Data Plotter Application created in Python using Plotly and Dash. Originally purposed as a Ground-Station Visualisation Tool for Data Telemetry. 

## OVERVIEW
Reads a locally accessed CSV file containing appropriately formatted data, and iterates over the CSV endlessly. Displays the most recent data-readings, and plots a rolling window of 100 readings for each data-type.

<br>
<p align="center">
<img width="764" alt="dataplotterimg2" src="https://github.com/sav-1305/Data-Plotter-Dash/assets/115809311/4a9f5a2d-0388-4739-91a5-7bfff3c8bf7d">
</p>
<p align="center"> fig. Updating-Plot of Velocity Data </p>
<br>

## HOW TO USE
- Install required Dependencies:
  
  ```
  from dash import Dash, dcc, html
  from dash.dependencies import Input, Output
  import pandas as pd
  import plotly.express as px
  from datetime import datetime
  import time
  import dash_bootstrap_components as dbc
  ```
- Run the ```plotter/plotter.py``` file, and open the local-host server (127.0.0.1)

## FUTURE WORK
- Live Communication Protocol Integration
- Scalability for other System-Applications
