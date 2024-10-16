if True:
    import sys

    sys.path.append("../../../")
    import dash
    import json
    from dash import html
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileSwipeAction(
            html.Div(style=style(height=80, background="#f5f5f5")),
            id="input",
            leftActions=[
                {"key": "按钮1", "color": "light", "text": "按钮1"},
                {"key": "按钮2", "color": "weak", "text": "按钮2"},
                {"key": "按钮3", "color": "primary", "text": "按钮3"},
            ],
            rightActions=[
                {"key": "按钮4", "color": "success", "text": "按钮4"},
                {"key": "按钮5", "color": "warning", "text": "按钮5"},
                {"key": "按钮6", "color": "danger", "text": "按钮6"},
            ],
        ),
        html.Pre(id="output"),
    ],
    style=style(padding=50),
)


@app.callback(
    Output("output", "children"),
    Input("input", "actionEvent"),
    prevent_initial_call=True,
)
def output(actionEvent):
    return json.dumps(actionEvent, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)
