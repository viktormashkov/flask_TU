from flask import Flask
from flask import render_template
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
@app.route('/fruits')
def fruits():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('fruit_page.html', graph=graph, title='Fruits in North America')


@app.route('/vegetables')
def vegetables():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('vegetable_page.html', graph=graph, title='Vegetables in Europe')


@app.route('/earthquakes')
def earthquakes():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

    fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                            center=dict(lat=0, lon=180), zoom=0,
                            mapbox_style="stamen-terrain")
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('earthquake_page.html', graph=graph, title='Earthquake heatmap')
