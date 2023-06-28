import dash
from dash import html
import feffery_antd_mobile_components as famc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        famc.MobileSpace(
            [
                html.Div(
                    'TabBar',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileTabBar(
                    items=[
                        {
                            'key': f'选项{i}',
                            'title': f'选项{i}'
                        }
                        for i in range(1, 4)
                    ]
                ),
                famc.MobileTabBar(
                    items=[
                        {
                            'key': '首页',
                            'title': '首页',
                            'icon': famc.MobileIcon(
                                icon='AppOutline'
                            ),
                            'badge': 6
                        },
                        {
                            'key': '待办',
                            'title': '待办',
                            'icon': famc.MobileIcon(
                                icon='UnorderedListOutline'
                            ),
                            'badge': '6'
                        },
                        {
                            'key': '消息',
                            'title': '消息',
                            'icon': famc.MobileIcon(
                                icon='MessageOutline'
                            ),
                            'badge': '99+'
                        },
                        {
                            'key': '我的',
                            'title': '我的',
                            'icon': famc.MobileIcon(
                                icon='UserOutline'
                            ),
                            'badge': 'dot'
                        }
                    ]
                ),

                html.Div(
                    'SideBar',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSideBar(
                    items=[
                        {
                            'key': f'选项{i}',
                            'title': f'选项{i}'
                        }
                        for i in range(1, 4)
                    ]
                ),
                famc.MobileSideBar(
                    items=[
                        {
                            'key': '选项1',
                            'title': '选项1',
                            'badge': 6
                        },
                        {
                            'key': '选项2',
                            'title': '选项2',
                            'badge': '99+'
                        },
                        {
                            'key': '选项3',
                            'title': '选项3',
                            'badge': 'dot'
                        }
                    ]
                ),

                html.Div(
                    'NavBar',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileNavBar(
                    '标题示例'
                ),
                famc.MobileNavBar(
                    '标题示例',
                    back='返回'
                ),
                famc.MobileNavBar(
                    '标题示例',
                    back='返回',
                    backArrow=False
                ),
                famc.MobileNavBar(
                    '标题示例',
                    back='返回',
                    backArrow=famc.MobileIcon(
                        icon='CloseOutline'
                    )
                ),

                html.Div(
                    'JumboTabs',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileJumboTabs(
                            items=[
                                {
                                    'title': '水果',
                                    'key': '水果',
                                    'children': '水果',
                                    'description': '描述文案',
                                },
                                {
                                    'title': '蔬菜',
                                    'key': '蔬菜',
                                    'children': '蔬菜',
                                    'description': '描述文案'
                                },
                                {
                                    'title': '动物',
                                    'key': '动物',
                                    'children': '动物',
                                    'description': '描述文案',
                                    'disabled': True
                                }
                            ],
                            activeKey='蔬菜'
                        ),
                        famc.MobileJumboTabs(
                            items=[
                                {
                                    'title': value,
                                    'key': value,
                                    'description': '描述文案',
                                }
                                for value in [
                                    'Espresso', 'Coffee Latte', 'Cappuccino',
                                    'Americano', 'Flat White', 'Caramel Macchiato',
                                    'Cafe Mocha'
                                ]
                            ]
                        )
                    ],
                    direction='vertical',
                    style={
                        'width': '100vw'
                    }
                ),

                html.Div(
                    'CapsuleTabs',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileCapsuleTabs(
                            items=[
                                {
                                    'title': '水果',
                                    'key': '水果',
                                    'children': '水果',
                                },
                                {
                                    'title': '蔬菜',
                                    'key': '蔬菜',
                                    'children': '蔬菜',
                                },
                                {
                                    'title': '动物',
                                    'key': '动物',
                                    'children': '动物',
                                }
                            ],
                            activeKey='蔬菜'
                        ),
                        famc.MobileCapsuleTabs(
                            items=[
                                {
                                    'title': value,
                                    'key': value
                                }
                                for value in [
                                    'Espresso', 'Coffee Latte', 'Cappuccino',
                                    'Americano', 'Flat White', 'Caramel Macchiato',
                                    'Cafe Mocha'
                                ]
                            ]
                        )
                    ],
                    direction='vertical',
                    style={
                        'width': '100vw'
                    }
                ),

                html.Div(
                    'Grid',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileGrid(
                    [
                        *[
                            famc.MobileGridItem(
                                f'item{i}',
                                span=2,
                                style={
                                    'background': '#c5f6fa',
                                    'border': '1px solid #ffd43b',
                                    'padding': 8,
                                    'textAlign': 'center',
                                    'fontSize': 16
                                }
                            )
                            for i in range(1, 5)
                        ],
                        famc.MobileGridItem(
                            'item5',
                            span=4,
                            style={
                                'background': '#c5f6fa',
                                'border': '1px solid #ffd43b',
                                'padding': 8,
                                'textAlign': 'center',
                                'fontSize': 16
                            }
                        )
                    ],
                    columns=4,
                    gap=5
                ),

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
    app.run(debug=True)
