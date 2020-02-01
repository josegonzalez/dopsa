import os
import dash
from dash.dependencies import Input, Output
import dash_enterprise_auth as auth
import dash_core_components as dcc
import dash_html_components as html

from components import Column, Header, Row

app = dash.Dash(
    __name__
)

server = app.server  # Expose the server variable for deployments

options = [{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']]

# Standard Dash app code below
app.layout = html.Div(className='container', children=[

    Header('Sample App', app),

    Row([
        Column(width=4, children=[
            dcc.Dropdown(
                id='dropdown',
                options=options,
                value='LA'
            )
        ]),
        Column(width=8, children=[
            dcc.Graph(id='graph')
        ])
    ])
])


@app.callback(Output('title', 'children'), [Input('title', 'id')])
def give_name(title):
    username = auth.get_username()
    if username:
        return '{}\'s Sample App'.format(username)
    return 'Anonymous Sample App'


@app.callback(Output('graph', 'figure'),
              [Input('dropdown', 'value')])
def update_graph(value):
    return {
        'data': [{
            'x': [1, 2, 3, 4, 5, 6],
            'y': [3, 1, 2, 3, 5, 6]
        }],
        'layout': {
            'title': value,
            'margin': {
                'l': 60,
                'r': 10,
                't': 40,
                'b': 60
            }
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
