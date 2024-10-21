if True:
    import sys

    sys.path.append('../../../')
    import dash
    from dash import html
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileButton(
            '打开面板', id='open-action-sheet'
        ),
        famc.MobileActionSheet(
            id='action-sheet-demo',
            actions=[
                {
                    'key': '操作1',
                    'text': '操作1',
                    'disabled': True,
                },
                {
                    'key': '操作2',
                    'text': '操作2',
                    'description': '这是操作2',
                },
                {
                    'key': '操作3',
                    'text': '操作3',
                    'danger': True,
                    'bold': True,
                },
            ],
            closeOnAction=True,
            visible=True,
            extra='extra示例内容',
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('action-sheet-demo', 'visible'),
    Input('open-action-sheet', 'nClicks'),
    prevent_initial_call=True,
)
def open_action_sheet(nClicks):
    return True


if __name__ == '__main__':
    app.run(debug=True)
