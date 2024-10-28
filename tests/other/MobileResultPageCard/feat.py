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
        famc.MobileResultPage(
            [
                famc.MobileResultPageCard(
                    style=style(height=128, marginTop=12)
                )
            ]
            * 4,
            title='操作成功',
            description='内容详情可折行，建议不超过两行建议不超过两行建议不超过两行',
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
