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
                famc.MobilePickerView(
                    id='picker-view-dmeo',
                    columns=[
                        [
                            {'label': value, 'value': value}
                            for value in [
                                '周一',
                                '周二',
                                '周三',
                                '周四',
                                '周五',
                                '周六',
                                '周日',
                            ]
                        ],
                        [
                            {'label': value, 'value': value}
                            for value in [
                                '上午',
                                '下午',
                            ]
                        ],
                    ],
                    defaultValue=['周三', '下午'],
                ),
                html.Span(id='picker-view-dmeo-output'),
            ],
            direction='vertical',
            block=True,
        )
    ],
    style=style(padding=50),
)


@app.callback(
    Output('picker-view-dmeo-output', 'children'),
    Input('picker-view-dmeo', 'value'),
)
def output(value):
    return str(value)


if __name__ == '__main__':
    app.run(debug=True)
