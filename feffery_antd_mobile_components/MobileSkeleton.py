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


class MobileSkeleton(Component):
    """A MobileSkeleton component.
骨架屏组件MobileSkeleton

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- animated (boolean; default False):
    是否开启动画效果  默认：False.

- debug (boolean; default False):
    是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印prop信息  默认：False.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    设置自定义监听组件的模式，可选的有'default'、'exclude'、'include'  默认：'default'.

- excludeProps (list of strings; optional):
    设置需要忽略输出监听过程的组件信息列表，仅在listenPropsMode为'exclude'时生效.

- includeProps (list of strings; optional):
    设置需要包含输出监听过程的组件信息列表，仅在listenPropsMode为'include'时生效."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSkeleton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        animated: typing.Optional[bool] = None,
        debug: typing.Optional[bool] = None,
        listenPropsMode: typing.Optional[Literal["default", "exclude", "include"]] = None,
        excludeProps: typing.Optional[typing.Sequence[str]] = None,
        includeProps: typing.Optional[typing.Sequence[str]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'animated', 'debug', 'listenPropsMode', 'excludeProps', 'includeProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'animated', 'debug', 'listenPropsMode', 'excludeProps', 'includeProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileSkeleton, self).__init__(children=children, **args)

setattr(MobileSkeleton, "__init__", _explicitize_args(MobileSkeleton.__init__))
