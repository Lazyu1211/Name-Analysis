from dash import Dash, html, dcc
import plotly.express as px
from utill import get_male_top10, get_female_top10, get_19male_top10, get_19female_top10, get_50male_top10, get_50female_top10, get_00male_top10, get_00female_top10, get_15male_top10, get_15female_top10

def render(app):
    df = get_male_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Male Names In the USA')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")

def render1(app):
    df = get_female_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Female Names In the USA')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart1")

def render2(app):
    df = get_19male_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Male Names In the USA From 1880 To 1900')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart2")

def render3(app):
    df = get_19female_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Female Names In the USA From 1880 To 1900')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart3")

def render4(app):
    df = get_50male_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Male Names In the USA From 1900 To 1950')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart4")

def render5(app):
    df = get_50female_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Female Names In the USA From 1900 To 1950')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart5")

def render6(app):
    df = get_00male_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Male Names In the USA From 1950 To 2000')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart6")

def render7(app):
    df = get_00female_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Female Names In the USA From 1950 To 2000')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart7")

def render8(app):
    df = get_15male_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Male Names In the USA From 2000 To 2015')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart8")

def render9(app):
    df = get_15female_top10()
    fig = px.pie(df, values = 'Number', names = df.index, color="Number", title = 'Top 10 Female Names In the USA From 2000 To 2015')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart9")