if True:
    import sys

    sys.path.append('../../../')
    import dash
    from dash import html
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileSpace(
            [
                famc.MobileMockPhone(
                    html.Iframe(
                        src='https://wap.baidu.com/',
                        style=style(
                            border='none',
                            height='100%',
                            width='100%',
                        ),
                    )
                ),
            ],
            direction='vertical',
        )
    ],
    style=style(padding=50),
)

if __name__ == '__main__':
    app.run(debug=True)
