import dash
from dash import html
import feffery_antd_mobile_components as famc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobilePopover(
            famc.MobileButton(
                '测试'
            ),
            content='气泡弹出框示例',
            placement='right',
            mode='dark'
        ),
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
        html.Div(id='content'),
        famc.MobileSpace(
            [
                famc.MobileSpace(
                    [
                        famc.MobileProgressCircle(
                            percent=80
                        ),
                        famc.MobileProgressCircle(
                            '50%',
                            percent=50
                        )
                    ]
                ),
                famc.MobileSpace(
                    [
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--track-width': '2px'
                            }
                        ),
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--track-width': '4px'
                            }
                        ),
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--track-width': '6px'
                            }
                        ),
                    ]
                ),
                famc.MobileSpace(
                    [
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--size': '20px'
                            }
                        ),
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--size': '50px'
                            }
                        ),
                        famc.MobileProgressCircle(
                            percent=75,
                            style={
                                '--size': '100px'
                            }
                        ),
                    ],
                    align='center'
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'background': '#fafbfc',
        'minHeight': '100vh',
        'padding': 24
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
