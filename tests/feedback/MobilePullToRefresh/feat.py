if True:
    import sys

    sys.path.append("../../../")
    import dash
    import time
    from dash import html
    import feffery_antd_mobile_components as famc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobilePullToRefresh(
            html.Div(id="output", style=style(height="150vh", background="#f0f0f0")),
            id="pull-to-refresh-demo",
        )
    ]
)


@app.callback(
    Output("output", "children"),
    Output("pull-to-refresh-demo", "stopRefreshing"),
    Input("pull-to-refresh-demo", "refreshCount"),
    prevent_initial_call=True,
)
def update_output(refreshCount):
    time.sleep(1)
    return f"refreshCount: {refreshCount}", True


if __name__ == "__main__":
    app.run(debug=True)
