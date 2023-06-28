import dash
from dash import html
import feffery_antd_mobile_components as famc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileSpace(
            [
                html.Div(
                    'Divider',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileDivider(),

                        famc.MobileDivider(
                            '示例分割线'
                        ),

                        famc.MobileDivider(
                            'left',
                            contentPosition='left'
                        ),

                        famc.MobileDivider(
                            'right',
                            contentPosition='right'
                        ),

                        famc.MobileDivider(
                            '自定义样式',
                            style={
                                'color': '#1677ff',
                                'borderColor': '#1677ff',
                                'borderStyle': 'dashed'
                            }
                        ),

                        html.Div(
                            [
                                '示例',
                                famc.MobileDivider(
                                    direction='vertical'
                                ),
                                '示例',
                                famc.MobileDivider(
                                    direction='vertical',
                                    style={
                                        'color': '#1677ff',
                                        'borderColor': '#1677ff'
                                    }
                                ),
                                '示例'
                            ]
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                html.Div(
                    'AutoCenter',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileAutoCenter(
                            'id eiusmod aute'
                        ),
                        famc.MobileAutoCenter(
                            'Ea anim culpa aliqua veniam do non do laboris aliqua. Dolore anim aute consequat consequat. Officia duis pariatur occaecat reprehenderit esse cillum voluptate do id eiusmod reprehenderit enim magna. Labore reprehenderit adipisicing veniam enim sit ullamco fugiat incididunt laborum veniam labore. Ipsum velit exercitation sunt sit velit. Commodo irure nulla dolor nisi culpa esse nisi voluptate amet aliquip veniam nostrud do labore mollit. Esse aliquip laboris mollit fugiat fugiat id eu magna commodo dolore nostrud do consectetur eiusmod exercitation. Sit anim sunt labore voluptate id mollit Lorem non minim elit non eiusmod aute. Dolore eiusmod consequat nostrud reprehenderit cillum ullamco fugiat officia cupidatat.'
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

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
                ),

                html.Div(
                    '图标示例',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileIcon(
                            icon=icon
                        )
                        for icon in
                        [
                            'AddCircleOutline',
                            'AddOutline',
                            'AddSquareOutline',
                            'AppstoreOutline',
                            'PicturesOutline',
                            'FilterOutline'
                        ]
                    ],
                    wrap=True,
                    block=True,
                    style={
                        'background': 'white',
                        'padding': '8px 5px',
                        'fontSize': 32
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
