import plotly.express as px
import csv 
import numpy as np
import pandas as pd

def getDataSource(datapath):
    attendance = []
    marks = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            marks.append(float(i["Marks In Percentage"]))
            attendance.append(float(i["Days Present"]))

    return {"x": marks, "y": attendance}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between MARKS and ATTENDANCE: ", correlation[0, 1])

def setup():
    datapath = "data1.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

setup()

def plotgraph():
    df = pd.read_csv("data1.csv")
    fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
    fig.show()

plotgraph()