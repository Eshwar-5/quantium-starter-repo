from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# --- Data Preparation ---
# Ensure the path matches your local setup
df = pd.read_csv("formatted_output.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# --- App Layout ---
app.layout = html.Div(className="container", children=[
    html.H1(
        children='Soul Foods: Pink Morsel Visualizer',
        className="header"
    ),

    # The Radio Button Filter
    html.Div(className="control-box", children=[
        html.Label("Filter by Region:", className="control-label"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",  # Default selection
            inline=True,
            className="radio-items"
        ),
    ]),

    # The Graph (now controlled by the callback)
    dcc.Graph(id='sales-line-chart')
])


# --- Callbacks ---
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    # Filter logic
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create the figure based on filtered data
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales: {selected_region.capitalize()}",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales (USD)",
        transition_duration=500  # Smooths the update animation
    )

    # Use a custom color to make it "Pink Morsel" themed
    fig.update_traces(line_color="#e91e63")

    return fig


if __name__ == '__main__':
    app.run(debug=True)