from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_all_sex, get_19_sex, get_50_sex, get_00_sex, get_15_sex, get_15male_bar, get_15female_bar


def render(app):
    df = get_all_sex()
    fig = px.bar(
        df,
        x = "Number",
        y = df.index,
        color= "Number",
        title="Sex Total from 1880 to 2015")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume")

def render1(app):
    df = get_19_sex()
    fig = px.bar(
        df,
        x = "Number",
        y = df.index,
        color= "Number",
        title="Sex Total from 1880 to 1900")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume1")

def render2(app):
    df = get_50_sex()
    fig = px.bar(
        df,
        x = "Number",
        y = df.index,
        color= "Number",
        title="Sex Total from 1900 to 1950")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume2")

def render3(app):
    df = get_00_sex()
    fig = px.bar(
        df,
        x = "Number",
        y = df.index,
        color= "Number",
        title="Sex Total from 1950 to 2000")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume3")

def render4(app):
    df = get_15_sex()
    fig = px.bar(
        df,
        x = "Number",
        y = df.index,
        color= "Number",
        title="Sex Total from 2000 to 2015")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume4")

def render5(app):
    df = get_15male_bar()

    @app.callback(
        Output("bar_volume5","children"),
        Input("male_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Name in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Name selected", color="danger")
                ,id="bar_volume5")
            
        fig = px.bar(
            filtered_data,
            x="Name", 
            y="Number",
            orientation='v',
            color = "Number",
            title = "Top 10 Male Names In the USA From 2000 To 2015"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume5")
    return html.Div(id="bar_volume5")

def render6(app):
    df = get_15female_bar()

    @app.callback(
        Output("bar_volume6","children"),
        Input("female_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Name in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Name selected", color="danger")
                ,id="bar_volume5")
            
        fig = px.bar(
            filtered_data,
            x="Name", 
            y="Number",
            orientation='v',
            color = "Number",
            title = "Top 10 Female Names In the USA From 2000 To 2015"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume6")
    return html.Div(id="bar_volume6")