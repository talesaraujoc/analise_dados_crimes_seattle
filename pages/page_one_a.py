from dash import dash, html, dcc, Output, Input, State, dash_table, callback, register_page
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import load_figure_template

import pandas as pd
import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag

from globals import *


# Servidor
#load_figure_template("minty")

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css"])
#server = app.server

register_page(__name__, name="1.1", path='/page_one_a')



# DataFrame =================



########## Pré-layout ================



# Layout    =================
#app.layout = html.Div([
layout = html.Div([
    html.Div([
        html.H1("O número de crimes em Seattle aumenta conforme a população cresce?", className="main-title")
    ], className="header"),

    html.Div([
        dbc.Row(dcc.Graph()),

        dbc.Row()
    ], className="content-wrapper")


], className="main-container")








# Callbacks =================



# Servidor  =================
#if __name__ == '__main__':
#    app.run_server(debug=False)