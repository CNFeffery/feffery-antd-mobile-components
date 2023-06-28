import dash
from dash import html
import feffery_antd_mobile_components as famc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            '小彭❤️小庄',
            style={
                'color': '#697b8c',
                'textAlign': 'center',
                'fontSize': 18
            }
        ),
        famc.MobileSpace(
            [
                html.Div(
                    '颜色状态',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileButton(
                            color,
                            color=color
                        )
                        for color in
                        ['default', 'primary', 'success', 'warning', 'danger']
                    ],
                    wrap=True,
                    block=True,
                    style={
                        'background': 'white',
                        'padding': '8px 5px'
                    }
                ),

                html.Div(
                    '填充模式',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileButton(
                            fill,
                            fill=fill,
                            color='primary'
                        )
                        for fill in
                        ['solid', 'outline', 'none']
                    ],
                    wrap=True,
                    block=True,
                    style={
                        'background': 'white',
                        'padding': '8px 5px'
                    }
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'minHeight': '100vh',
        'background': '#fafbfc'
    }
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
