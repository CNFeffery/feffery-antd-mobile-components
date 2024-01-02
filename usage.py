import dash
from dash import html
import feffery_antd_mobile_components as famc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileFloatingBubble(
            famc.MobileIcon(
                icon='UnorderedListOutline',
                style={
                    'fontSize': 32
                }
            ),
            id='floating-bubble',
            axis='xy',
            magnetic='x',
            style={
                '--initial-position-bottom': '124px',
                '--initial-position-right': '24px',
                '--edge-distance': '24px',
            }
        ),
        html.Div(id='content')
    ],
    style={
        'minHeight': '100vh',
        'background': '#fafbfc'
    }
)


@app.callback(
    Output('content', 'children'),
    Input('floating-bubble', 'nClicks')
)
def demo(nClicks):

    return f'nClicks: {nClicks}'


if __name__ == '__main__':
    app.run(debug=True)
