if True:
    import sys

    sys.path.append('../../../')
    import dash
    from dash import html
    from dash.dependencies import Input, Output
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileSpace(
            [
                famc.MobileStepper(
                    id='stepper-demo',
                    digits=3,
                    style=style(width='100%'),
                ),
                html.Span(id='stepper-demo-output'),
            ],
            direction='vertical',
            block=True,
        )
    ],
    style=style(padding=50),
)


@app.callback(
    Output('stepper-demo-output', 'children'),
    Input('stepper-demo', 'value'),
)
def output(value):
    return str(value)


if __name__ == '__main__':
    app.run(debug=True)
