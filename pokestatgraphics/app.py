
import pandas as pd
from flask import Flask, render_template, request
from .models import df, G7
from .gaussians import VIEWS

df_rudy = pd.read_csv(G7)

def create_app():
    ''' create and configure an instance of the Flask application '''
    app = Flask(__name__)
    
    @app.route("/")
    def root():
        return render_template('base.html', title='Home', dat=df.values)

    @app.route("/gaussians")
    @app.route("/gaussians/<name>")
    def gaussians(name):
        d = {True: VIEWS[name]}

        return render_template('base.html', dat=df.values, view=VIEWS[name], ifA=True, d=d)  

    return app
