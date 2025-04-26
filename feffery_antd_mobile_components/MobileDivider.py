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


class MobileDivider(Component):
    """A MobileDivider component.
分割线组件MobileDivider

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- contentPosition (a value equal to: 'center', 'left', 'right'; default 'center'):
    用于设置当前分割线中内容的位置，仅在水平方向展示时有效  可选的有'center'、'left'、'right'
    默认：'center'.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于设置当前分割线的展示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileDivider'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        contentPosition: typing.Optional[Literal["center", "left", "right"]] = None,
        direction: typing.Optional[Literal["horizontal", "vertical"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'contentPosition', 'direction']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'contentPosition', 'direction']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileDivider, self).__init__(children=children, **args)

setattr(MobileDivider, "__init__", _explicitize_args(MobileDivider.__init__))
