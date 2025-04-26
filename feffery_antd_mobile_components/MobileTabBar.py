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


class MobileTabBar(Component):
    """A MobileTabBar component.
标签栏组件MobileTabBar

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
        必填，用于设置当前选项对应的标题内容.

    - icon (a list of or a singular dash component, string or number; optional):
        用于设置当前选项对应的额外图标.

    - badge (a list of or a singular dash component, string or number; optional):
        用于为当前选项设置额外的徽标信息  特别地，当传入'dot'时会渲染小红点徽标.

- activeKey (string; optional):
    用于设置或监听当前被激活的选项对应key值.

- defaultActiveKey (string; optional):
    用于设置初始化时，处于被激活状态的选项对应key值  默认激活items中按顺序第一位的选项.

- safeArea (boolean; default False):
    用于设置是否开启安全区适配功能  默认：False."""
    _children_props = ['items[].title', 'items[].icon', 'items[].badge']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileTabBar'
    Items = TypedDict(
        "Items",
            {
            "key": str,
            "title": ComponentType,
            "icon": NotRequired[ComponentType],
            "badge": NotRequired[ComponentType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        items: typing.Optional[typing.Sequence["Items"]] = None,
        activeKey: typing.Optional[str] = None,
        defaultActiveKey: typing.Optional[str] = None,
        safeArea: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'items', 'activeKey', 'defaultActiveKey', 'safeArea']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'items', 'activeKey', 'defaultActiveKey', 'safeArea']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileTabBar, self).__init__(**args)

setattr(MobileTabBar, "__init__", _explicitize_args(MobileTabBar.__init__))
