# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class MobileCollapse(Component):
    """A MobileCollapse component.
折叠面板组件MobileCollapse

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- items (list of dicts; optional):
    用于定义内部各选项相关信息.

    `items` is a list of dicts with keys:

    - key (string; required):
        必填，用于设置当前选项对应的唯一标识值.

    - title (a list of or a singular dash component, string or number; required):
        必填，用于设置当前选项对应的左侧标题栏内容.

    - children (a list of or a singular dash component, string or number; optional):
        可选，用于设置当前选项对应的内容.

    - disabled (boolean; optional):
        用于设置是否禁用当前选项  默认：False.

    - forceRender (boolean; optional):
        用于设置初始化时，若当前选项不可见，是否对其对应的children内容进行渲染  默认：False.

    - destroyOnClose (boolean; optional):
        用于设置当前选项被隐藏后，是否对其children内容进行销毁  默认：False.

    - arrow (a list of or a singular dash component, string or number; optional):
        用于为当前项自定义展开图标元素，传入None时会隐藏图标.

- accordion (boolean; optional):
    用于设置是否开启手风琴模式，开启后展开新的折叠面板会自动关闭先前展开的面板  默认：False.

- activeKey (string | list of strings; optional):
    用于设置或监听当前被激活的选项对应key值.

- defaultActiveKey (string | list of strings; optional):
    用于设置初始化时，处于被激活状态的选项对应key值  默认激活items中按顺序第一位的选项.

- stretch (boolean; optional):
    用于设置选项卡头部是否拉伸  默认：True."""
    _children_props = ['items[].title', 'items[].children', 'items[].arrow']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCollapse'
    Items = TypedDict(
        "Items",
            {
            "key": str,
            "title": ComponentType,
            "children": NotRequired[ComponentType],
            "disabled": NotRequired[bool],
            "forceRender": NotRequired[bool],
            "destroyOnClose": NotRequired[bool],
            "arrow": NotRequired[ComponentType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        items: typing.Optional[typing.Sequence["Items"]] = None,
        accordion: typing.Optional[bool] = None,
        activeKey: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        defaultActiveKey: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        stretch: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'items', 'accordion', 'activeKey', 'defaultActiveKey', 'stretch']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'items', 'accordion', 'activeKey', 'defaultActiveKey', 'stretch']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCollapse, self).__init__(**args)

setattr(MobileCollapse, "__init__", _explicitize_args(MobileCollapse.__init__))
