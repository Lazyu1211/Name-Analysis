from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_malelist, get_femalelist

def render(app):
    list_male = get_malelist()
    all_male = [{'label':i,'value':i} for i in list_male]
    @app.callback(
    Output(component_id='male_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_male(n):
        return list_male

    return html.Div(
        children=[
            html.H6("Select A Male Name"),
            dcc.Dropdown(
                options=all_male,
                multi=True,
                id = "male_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )

def render1(app):
    list_female = get_femalelist()
    all_female = [{'label':i,'value':i} for i in list_female]
    @app.callback(
    Output(component_id='female_dropdown', component_property='value'),
    Input(component_id='select_all_button1', component_property='n_clicks')
    )
    def update_all_female(n):
        return list_female

    return html.Div(
        children=[
            html.H6("Select A Female Name"),
            dcc.Dropdown(
                options=all_female,
                multi=True,
                id = "female_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button1",
                n_clicks=0
            )
        ]
    )