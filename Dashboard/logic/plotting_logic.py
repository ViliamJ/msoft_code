from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go


def total_plot():
    """
    View demonstrating how to display a graph object
    on a web page with Plotly.
    """
    df = data_total()
    x = df['Year']
    y = df['Profit']
    income = df['Income']
    expenses = df['Expenses']
    graph_labels = {"title": "Sumar - Zisk", "yaxis":'Zisk'}

    # List of graph objects for figure.
    # Each object will contain on series of data.
    fig = go.Figure()

    # Adding linear plot of y1 vs. x.
    fig.add_trace(
        go.Scatter(x=x, y=y, mode='lines', name='Line', customdata=[income, expenses])
    )

    fig.update_traces(
        hovertemplate="<br>".join([
            "Year: %{x}",
            "Profit: %{y}",
            "Income: %{customdata[0]}",
            "Expenes: %{customdata[1]}",
        ])
    )
    fig.update_layout(title_text=graph_labels["title"])
    # Setting layout of the figure.

    fig = summary_plot_slider(fig)

    return fig


def summary_plot_slider(fig):

    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    return fig

import pandas as pd
import random

def data_zoo():
    array = []
    for year in range(2000, 2020):
        expens = random.randint(100, 1000)
        income = random.randint(100, 2000)
        array.append([year, expens, income])

    zoo = pd.DataFrame(array, columns=['Year', 'Expenses', 'Income'])
    zoo['Profit'] = zoo['Income'] - zoo['Expenses']

    return zoo

def data_jakub():
    array = []
    for year in range(2000, 2020):
        expens = random.randint(100, 500)
        income = random.randint(100, 600)
        array.append([year, expens, income])

    jakub = pd.DataFrame(array, columns=['Year', 'Expenses', 'Income'])
    jakub['Profit'] = jakub['Income'] - jakub['Expenses']

    return jakub

def data_udrzba():
    array = []
    for year in range(2000, 2020):
        expens = random.randint(100, 5000)
        income = random.randint(100, 5500)
        array.append([year, expens, income])

    udrzba = pd.DataFrame(array, columns=['Year', 'Expenses', 'Income'])
    udrzba['Profit'] = udrzba['Income'] - udrzba['Expenses']

    return udrzba

def data_total():
    array = []
    for year in range(2000, 2020):
        expens = random.randint(15000, 18000)
        income = random.randint(15000, 30000)
        array.append([year, expens, income])

    total = pd.DataFrame(array, columns=['Year', 'Expenses', 'Income'])
    total['Profit'] = total['Income'] - total['Expenses']

    return total


def component_values(value):
    if value == "Zoo":
        data = data_zoo()
    elif value == "Jakub":
        data = data_jakub()
    else:
        data = data_udrzba()

    fig = go.Figure()

    # Adding linear plot of y1 vs. x.
    fig.add_trace(
        go.Scatter(x=data["Year"], y=data["Profit"], mode='lines', name='Line')
    )
    fig.update_layout(title_text=value)
    fig = summary_plot_slider(fig)

    return fig