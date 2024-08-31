import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [20000, 22000, 25000, 27500, 30000, 32000, 33000, 34000, 35500, 36000, 37000, 38000]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1('Monthly Revenue Dashboard'),
    
    dcc.Graph(
        id='revenue-bar-chart',
        figure=px.bar(df, x='Month', y='Revenue', title='Monthly Revenue')
    ),
    
    dcc.Graph(
        id='revenue-line-chart',
        figure=px.line(df, x='Month', y='Revenue', title='Monthly Revenue Trend')
    ),
    
    html.Div(id='revenue-summary')
])

# Callback to update the summary (optional)
@app.callback(
    Output('revenue-summary', 'children'),
    [Input('revenue-bar-chart', 'figure')]
)
def update_summary(fig):
    total_revenue = df['Revenue'].sum()
    avg_revenue = df['Revenue'].mean()
    return [
        html.P(f'Total Revenue: ${total_revenue:,.2f}'),
        html.P(f'Average Monthly Revenue: ${avg_revenue:,.2f}')
    ]

# Run the app
if __name__ == '__main__':
    # Specify the port (optional, default is 8050)
    port = 8050
    print(f"View the Dashboard: Open a web browser and go to http://127.0.0.1:{port}/")
    app.run_server(debug=True, port=port)
