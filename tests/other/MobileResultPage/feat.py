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
                famc.MobileResultPage(
                    title='操作成功',
                    description='内容详情可折行，建议不超过两行建议不超过两行建议不超过两行',
                ),
                famc.MobileResultPage(
                    title='操作成功',
                    description='内容详情可折行，建议不超过两行建议不超过两行建议不超过两行',
                    details=[
                        {
                            'label': '收款方',
                            'value': '张三',
                            'bold': True,
                        },
                        {
                            'label': '付款方式',
                            'value': '账户余额',
                        },
                        {
                            'label': '转账金额',
                            'value': '¥100.00',
                        },
                        {
                            'label': '转账金额',
                            'value': '¥100.00',
                        },
                        {
                            'label': '转账金额',
                            'value': '¥100.00',
                        },
                    ],
                ),
                famc.MobileResultPage(
                    title='操作成功',
                    description='内容详情可折行，建议不超过两行建议不超过两行建议不超过两行',
                    secondaryButtonText='辅助操作',
                    primaryButtonText='主要操作',
                ),
            ],
            direction='vertical',
            block=True,
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
