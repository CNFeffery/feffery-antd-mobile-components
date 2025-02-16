if True:
    import sys

    sys.path.append('../../../')
    import dash
    import time
    from dash import html
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileButton(
            '测试', id='input', color='primary'
        ),
        famc.MobileSkeleton(
            html.Div(id='output'),
            animated=True,
            style={'--height': '100px'},
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('output', 'children'),
    Input('input', 'nClicks'),
    prevent_initial_call=True,
)
def demo(nClicks):
    time.sleep(3)

    return nClicks


if __name__ == '__main__':
    app.run(debug=True)
