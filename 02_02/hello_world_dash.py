import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

# Read in data
data = pd.read_csv("/workspaces/python-dash/02_03/precious_metals_prices_2018_2021.csv", usecols=["DateTime","Gold"])

#Create a plotly figure for use by dcc.Grapf()
fig = px.line(data, x="DateTime", y="Gold", title="Precious Metal Prices 2018-2021")

app = dash.Dash(__name__)
app.title = "Precious Metal Prices 2018-2021"

#app.layout = html.P("Hello Dash!")
app.layout = html.Div(
    id="app-container",
    children=[
        html.H1("Precious Metal Prices 2018-2021"),
        html.P("Results in USD/oz"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
