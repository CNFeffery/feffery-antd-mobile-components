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
        famc.MobileButton('打开对话框', id='open-dialog'),
        famc.MobileDialog(
            id='dialog-demo',
            actions=[
                {'key': '操作1', 'text': '操作1'},
                {'key': '操作2', 'text': '操作2'},
                [
                    {'key': '操作3-1', 'text': '操作3-1'},
                    {
                        'key': '操作3-2',
                        'text': '操作3-2',
                        'danger': True,
                        'bold': True,
                    },
                ],
            ],
            closeOnAction=True,
            closeOnMaskClick=True,
            header='对话框标题',
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('dialog-demo', 'visible'),
    Input('open-dialog', 'nClicks'),
    prevent_initial_call=True,
)
def open_dialog(nClicks):
    return True


if __name__ == '__main__':
    app.run(debug=True)
