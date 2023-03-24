from dash import Dash,html,dcc
import os   
import dash_bootstrap_components as dbc
from components import pie_charts, bar_charts, dropdown

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNbwyTJ1I2u71KU3eJqFst5ZFvqkL2MKq-BA&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVL33WGAny31DzeNtBmdnSqAYuDJW0cXNXQg&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "Name Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center', 'color':'red'}
              ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'})
,       
    ],className="mt-4"),
        dbc.Row([
            html.H2(
                "Top 10 male and female names in USA from 1880 to 2015 !!!",
                className="header-description", style={'margin-top': '10px', 'text-align': 'center'}
                ),
            html.H6(
                "Top Three Male and Female Names",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(1570954, 5120990, step=None, marks={1570954:'Patricia', 1610948:'Elizabeth', 4118058:'Mary', 4803068:'Robert', 5095674:'John', 5120990:'James'}, value=5,id='my-slider', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container'),
            dbc.Col(bar_charts.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render1(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 male and female names in USA from 1880 to 1900 !!!",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            html.H6(
                "Top Three Male and Female Names",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(59738, 222804, step=None, marks={59738:'Margaret', 93420:'Anna', 222804:'Mary', 157125:'William', 170616:'John', 104780:'James'}, value=5,id='my-slider1', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container1'),
            dbc.Col(bar_charts.render1(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render2(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render3(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 male and female names in USA from 1900 to 1950 !!!",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            html.H6(
                "Top Three Male and Female Names",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(846535, 2554792, step=None, marks={846535:'Barbara', 958065:'Dorothy', 2554792:'Mary', 2200063:'Robert', 2224324:'John', 2195545:'James'}, value=5,id='my-slider2', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container2'),
            dbc.Col(bar_charts.render2(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render4(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render5(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 male and female names in USA from 1950 to 2000 !!!",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            html.H6(
                "Top Three Male and Female Names",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(951507, 3504104, step=None, marks={951507:'Lisa', 1378134:'Jennifer', 1278426:'Mary', 3504104:'Michael', 2586880:'David', 2574582:'James'}, value=5,id='my-slider3', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container3'),
            dbc.Col(bar_charts.render3(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render6(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render7(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 male and female names in USA from 2000 to 2015 !!!",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            html.H6(
                "Top Three Male and Female Names",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(250868, 370101, step=None, marks={250868:'Madison', 279987:'Emma', 291475:'Emily', 296231:'Joshua', 331481:'Michael', 370101:'Jacob'}, value=5,id='my-slider4', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container4'),
            dbc.Col(bar_charts.render4(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render8(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render9(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "How many people called these popular names from 2000 to 2015 in the United States?",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render(app),lg=6, style={'margin-top': '30px', 'text-align': 'left'}),
            dbc.Col(dropdown.render1(app),lg=6, style={'margin-top': '30px', 'text-align': 'left'}),
            dbc.Col(bar_charts.render5(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render6(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'})
        ],className="mt-4"),
    ])