import dash
from dash import html
import feffery_antd_mobile_components as famc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileButton(
            '按钮'
        )
    ],
    style={
        'padding': 100
    }
)

if __name__ == '__main__':
    app.run(debug=True)