import dash
from dash import html
import feffery_antd_mobile_components as famc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

demo_image = 'https://images.unsplash.com/photo-1567945716310-4745a6b7844b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=60'

app.layout = html.Div(
    [
        famc.MobileSpace(
            [
                html.Div(
                    'Swiper',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileSwiper(
                            items=[
                                {
                                    'key': f'子项{i}',
                                    'children': html.Div(
                                        f'子项{i}',
                                        style={
                                            'height': 200,
                                            'background': '#40a9ff',
                                            'opacity': 1 - 0.1*i,
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'color': 'white',
                                            'fontSize': 28
                                        }
                                    )
                                }
                                for i in range(1, 6)
                            ],
                            defaultIndex=2,
                            autoplayInterval=1000,
                            autoplay=True,
                            loop=True
                        ),
                        famc.MobileSwiper(
                            items=[
                                {
                                    'key': f'子项{i}',
                                    'children': html.Div(
                                        f'子项{i}',
                                        style={
                                            'height': 200,
                                            'background': '#40a9ff',
                                            'opacity': 1 - 0.1*i,
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'color': 'white',
                                            'fontSize': 28
                                        }
                                    )
                                }
                                for i in range(1, 6)
                            ],
                            defaultIndex=2,
                            autoplayInterval=1000,
                            autoplay=True,
                            loop=True,
                            direction='vertical',
                            style={
                                'height': 200
                            }
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                html.Div(
                    'Steps',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileSteps(
                            steps=[
                                {
                                    'title': f'步骤{i}'
                                }
                                for i in range(1, 5)
                            ]
                        ),
                        famc.MobileSteps(
                            steps=[
                                {
                                    'title': f'步骤{i}'
                                }
                                for i in range(1, 5)
                            ],
                            direction='vertical'
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                html.Div(
                    'PageIndicator',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobilePageIndicator(
                            total=5,
                            current=0
                        ),
                        famc.MobilePageIndicator(
                            total=5,
                            current=0,
                            direction='vertical'
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                html.Div(
                    'List',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileList(
                            title='基础用法',
                            items=[
                                {
                                    'key': f'子项{i}',
                                    'children': f'子项{i}'
                                }
                                for i in range(1, 4)
                            ]
                        ),
                        famc.MobileList(
                            title='可点击',
                            items=[
                                {
                                    'key': '账单',
                                    'children': '账单',
                                    'prefix': famc.MobileIcon(
                                        icon='UnorderedListOutline'
                                    ),
                                    'clickable': True
                                },
                                {
                                    'key': '总资产',
                                    'children': '总资产',
                                    'prefix': famc.MobileIcon(
                                        icon='PayCircleOutline'
                                    ),
                                    'clickable': True
                                },
                                {
                                    'key': '设置',
                                    'children': '设置',
                                    'prefix': famc.MobileIcon(
                                        icon='SetOutline'
                                    ),
                                    'clickable': True
                                }
                            ]
                        )
                    ],
                    direction='vertical',
                    block=True
                ),


                html.Div(
                    'ImageViwer',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileImage(
                    id='image-viewer-trigger',
                    src=demo_image
                ),
                famc.MobileImageViewer(
                    id='image-viewer',
                    image=demo_image
                ),

                html.Div(
                    'Image',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileImage(
                            src=demo_image
                        ),

                        famc.MobileSpace(
                            [
                                famc.MobileImage(
                                    src=demo_image,
                                    width=100,
                                    height=100,
                                    fit=fit
                                )
                                for fit in [
                                    'fill', 'contain', 'cover',
                                    'scale-down', 'none'
                                ]
                            ],
                            wrap=True
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                # html.Div(
                #     'FloatingPanel',
                #     style={
                #         'color': '#697b8c'
                #     }
                # ),
                # famc.MobileFloatingPanel(
                #     '内容' * 100,v
                #     anchors=[100, 0.5, 0.8, 1]
                # ),

                html.Div(
                    'Ellipsis',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileEllipsis(
                            content='巴拉巴拉'*100,
                            direction='middle'
                        ),
                        famc.MobileEllipsis(
                            content='巴拉巴拉'*100,
                            direction='end',
                            expandText='展开',
                            collapseText='收起',
                            rows=4
                        ),
                        famc.MobileEllipsis(
                            content='巴拉巴拉'*100,
                            direction='end',
                            expandText=[
                                '展开',
                                famc.MobileIcon(
                                    icon='DownOutline'
                                )
                            ],
                            collapseText=[
                                '收起',
                                famc.MobileIcon(
                                    icon='UpOutline'
                                )
                            ],
                            rows=4
                        )
                    ],
                    direction='vertical'
                ),

                html.Div(
                    'Collapse',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileCollapse(
                    items=[
                        {
                            'key': f'选项{i}',
                            'title': f'选项{i}',
                            'children': f'选项{i}示例内容'*25
                        }
                        for i in range(1, 6)
                    ]
                ),
                famc.MobileCollapse(
                    items=[
                        {
                            'key': f'手风琴选项{i}',
                            'title': f'手风琴选项{i}',
                            'children': f'手风琴选项{i}示例内容'*25
                        }
                        for i in range(1, 6)
                    ],
                    accordion=True
                ),

                html.Div(
                    'Card',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileCard(
                            '卡片内容',
                            title='标题测试'
                        )
                    ],
                    direction='vertical',
                    block=True
                ),

                html.Div(
                    'Avatar',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileSpace(
                    [
                        famc.MobileAvatar(
                            src='https://images.unsplash.com/photo-1548532928-b34e3be62fc6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&ixid=eyJhcHBfaWQiOjE3Nzg0fQ'
                        ),
                        famc.MobileAvatar(),
                        famc.MobileAvatar(
                            src='https://images.unsplash.com/photo-1548532928-b34e3be62fc6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&ixid=eyJhcHBfaWQiOjE3Nzg0fQ',
                            style={
                                '--size': '64px'
                            }
                        ),
                    ],
                    direction='vertical',
                    style={
                        'padding': 5
                    }
                ),


                html.Div(
                    'Tabs',
                    style={
                        'color': '#697b8c'
                    }
                ),
                famc.MobileTabs(
                    items=[
                        {
                            'key': f'选项{i}',
                            'title': f'选项{i}',
                            'children': f'选项{i}示例内容'*10
                        }
                        for i in range(1, 5)
                    ],
                    defaultActiveKey='选项3'
                ),

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


@app.callback(
    Output('image-viewer', 'visible'),
    Input('image-viewer-trigger', 'nClicks'),
    prevent_initial_call=True
)
def image_viewer_demo(nClicks):

    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
