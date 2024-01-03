import dash
from dash import html
import feffery_antd_mobile_components as famc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileInput(
            id='input-demo',
            placeholder='请输入',
            style={
                'width': '100%'
            }
        ),
        html.Div(
            id='input-demo-output'
        )
    ],
    style={
        'background': '#fafbfc',
        'minHeight': '100vh',
        'padding': 24
    }
)


@app.callback(
    Output('input-demo-output', 'children'),
    Input('input-demo', 'value')
)
def demo(value):

    return f'value: {value}'


if __name__ == '__main__':
    app.run(debug=True)
