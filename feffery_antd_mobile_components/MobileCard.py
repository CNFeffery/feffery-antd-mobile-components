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


class MobileCard(Component):
    """A MobileCard component.
卡片组件MobileCard

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- bodyClassName (string; optional):
    用于设置当前卡片body区域css类.

- bodyStyle (dict; optional):
    用于设置当前卡片body区域css样式.

- extra (a list of or a singular dash component, string or number; optional):
    用于为当前卡片设置头部右侧元素.

- headerClassName (string; optional):
    用于设置当前卡片头部区域css类.

- headerStyle (dict; optional):
    用于设置当前卡片头部区域css样式.

- title (a list of or a singular dash component, string or number; optional):
    用于为当前卡片设置头部左侧标题内容."""
    _children_props = ['extra', 'title']
    _base_nodes = ['extra', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCard'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        bodyClassName: typing.Optional[str] = None,
        bodyStyle: typing.Optional[dict] = None,
        extra: typing.Optional[ComponentType] = None,
        headerClassName: typing.Optional[str] = None,
        headerStyle: typing.Optional[dict] = None,
        title: typing.Optional[ComponentType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'bodyClassName', 'bodyStyle', 'extra', 'headerClassName', 'headerStyle', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'bodyClassName', 'bodyStyle', 'extra', 'headerClassName', 'headerStyle', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCard, self).__init__(children=children, **args)

setattr(MobileCard, "__init__", _explicitize_args(MobileCard.__init__))
