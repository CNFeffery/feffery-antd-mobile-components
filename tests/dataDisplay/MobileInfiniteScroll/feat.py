if True:
    import sys

    sys.path.append('../../../')
    import uuid
    import dash
    import time
    from dash import html, Patch
    import feffery_antd_mobile_components as famc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileList(
            id='list-demo',
            items=[
                {
                    'key': str(uuid.uuid4()),
                    'children': famc.MobileAutoCenter(
                        str(int(time.time()))
                    ),
                }
                for i in range(5)
            ],
        ),
        famc.MobileInfiniteScroll(
            id='infinite-scroll-demo',
        ),
    ]
)


@app.callback(
    Output('list-demo', 'items'),
    Output('infinite-scroll-demo', 'hasMore'),
    Output('infinite-scroll-demo', 'stopRefreshing'),
    Input('infinite-scroll-demo', 'refreshCount'),
    prevent_initial_call=True,
)
def update_output(refreshCount):
    time.sleep(2)
    p = Patch()
    p.extend(
        [
            {
                'key': str(uuid.uuid4()),
                'children': famc.MobileAutoCenter(
                    str(int(time.time()))
                ),
            }
            for i in range(10)
        ]
    )
    return [p, refreshCount <= 5, True]


if __name__ == '__main__':
    app.run(debug=True)
