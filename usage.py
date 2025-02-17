import dash
from dash import html
import feffery_antd_mobile_components as famc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = famc.Fragment(
    html.Div(
        [
            famc.MobileButton(
                '测试',
                id='button-demo',
                color='primary',
            ),
            html.Div(id='button-demo-output'),
        ],
        style={
            'background': '#fafbfc',
            'minHeight': '100vh',
            'padding': 24,
            'boxSizing': 'border-box',
        },
    )
)


@app.callback(
    Output('button-demo-output', 'children'),
    Input('button-demo', 'nClicks'),
    prevent_initial_call=True,
)
def button_demo(nClicks):
    return nClicks


if __name__ == '__main__':
    app.run(debug=True)
