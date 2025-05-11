import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Dash Starter App"),
    html.P("If you can see this, the setup is complete!")
])

if __name__ == "__main__":
    app.run_server(debug=True)
