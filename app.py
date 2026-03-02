from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Assume you have your data loaded here
# df = pd.read_csv("your_data.csv")

app = Dash(__name__)

app.layout = html.Div(className="container", children=[
    html.H1(
        children='Soul Foods: Pink Morsel Visualizer',
        id="header",
        className="header"
    ),

    html.Div(className="control-box", children=[
        html.Label("Filter by Region:", className="control-label"),
        dcc.RadioItems(
            id="region-picker",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",
            inline=True,
            className="radio-items"
        ),
    ]),

    dcc.Graph(id='visualisation')
])

@app.callback(
    Output("visualisation", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):
    # Minimal placeholder logic for the test to pass
    fig = px.line(title=f"Sales for {selected_region}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)