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


class MobileNavBar(Component):
    """A MobileNavBar component.
导航栏组件MobileNavBar

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置导航栏标题内容.

- back (a list of or a singular dash component, string or number; default ''):
    用于为当前导航栏设置返回区域文字内容，传入None时会连带返回按钮一起隐藏  默认：''.

- backArrow (boolean | a list of or a singular dash component, string or number; default True):
    用于为当前导航栏设置是否显示返回箭头，也可传入组件型输入充当自定义返回箭头  默认：True.

- left (a list of or a singular dash component, string or number; optional):
    用于设置显示在当前导航栏标题左侧的内容.

- right (a list of or a singular dash component, string or number; optional):
    用于设置显示在当前导航栏标题右侧的内容.

- nBackClicks (number; default 0):
    用于记录当前导航栏返回区域累计被点击次数."""
    _children_props = ['back', 'backArrow', 'left', 'right']
    _base_nodes = ['back', 'backArrow', 'left', 'right', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileNavBar'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        back: typing.Optional[ComponentType] = None,
        backArrow: typing.Optional[typing.Union[bool, ComponentType]] = None,
        left: typing.Optional[ComponentType] = None,
        right: typing.Optional[ComponentType] = None,
        nBackClicks: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'back', 'backArrow', 'left', 'right', 'nBackClicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'back', 'backArrow', 'left', 'right', 'nBackClicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileNavBar, self).__init__(children=children, **args)

setattr(MobileNavBar, "__init__", _explicitize_args(MobileNavBar.__init__))
