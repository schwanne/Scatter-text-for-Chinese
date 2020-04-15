# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:07:59 2020

@author: CNU074VP
"""

import os
os.chdir("D:/scattertext")

import pandas as pd
import numpy as np
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash
import sys
sys.path.append(os.path.abspath("./utils"))
from dash_helper import get_scattertext_html

from flask import Flask, render_template
#app_flask = Flask(__name__)

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
    style={"height": "100%"},
    children=[
        # Banner display
        html.Div(
            [
                # Change App Name here
                html.H2(
                    'Scatter Text Chart',
                    id='title',
                    className="eight columns",
                    style={
                        'text-decoration': 'none',
                        'color': 'white',
                        'font-family': 'Times New Roman',
                        "margin-left": "2%"
                    }
                ),


                html.A(
                    # dbc.Button("Learn More", id="learn-more-button", color="success"),
                    html.Button("LEARN MORE",
                                id="learn-more-button",
                                className="two columns",
                                style={
                                    'width': '120px',
                                    'height': '40px',
                                    'position': 'absolute',
                                                'top': '2%',
                                                'right': '15%'
                                }
                                ),
                    href="https://github.com/JasonKessler/scattertext",
                    style={'fontSize': 18}
                ),

                html.A(
                    html.Img(src="https://www.amway.com/medias/Amway-logo-124-42-.svg?context=bWFzdGVyfHJvb3R8NjIwMHxpbWFnZS9zdmcreG1sfGg5Zi9oZjQvODgxMzk1Mzg0MzIzMC5zdmd8NzQ0ZWE0YjlhNDkxYWI0YmZmMjdjMzE3YjJkNTE0N2IzYjA3NWEzYmQzYzVjZTg4ZDg4Y2VlOTA3NDZkMzUxNg",
                             className="two columns",
                             id="amway-logo",
                             style={
                                 'width': '160px',
                                 'height': '80px',
                                 'position': 'absolute',
                                 'top': '0px',
                                 'right': '2%'
                             }
                             ),
                    href='https://www.amway.com/'
                ),
            ],
            className="banner row",
        ),
        
        html.Div([html.A(href = "D:/scattertext/templates/protein_review_compare.html")])
        
        ])





@server.route("/")
def index():
    get_scattertext_html()        
    return render_template("protein_review_compare.html")


if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)
    
    
    
    
    
