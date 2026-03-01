from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# --- Data Preparation ---
df = pd.read_csv("../formatted_output.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# --- Create the Line Chart ---
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Trend")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales (USD)",
)

# --- App Layout ---
app.layout = html.Div(children=[
    html.H1(children='Soul Foods: Pink Morsel Visualizer', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)