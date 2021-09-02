import plotly.express as px
import csv 
import numpy as np
import pandas as pd

def getDataSource(datapath):
    coffee = []
    sleep = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["Sleep in hours"]))

    return {"x": coffee, "y": sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between COFFEE QUANTITY and SLEEP TIME: ", correlation[0, 1])

def setup():
    datapath = "data2.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

setup()

def plotgraph():
    df = pd.read_csv("data2.csv")
    fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
    fig.show()

plotgraph()