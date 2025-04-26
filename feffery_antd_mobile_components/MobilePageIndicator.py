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


class MobilePageIndicator(Component):
    """A MobilePageIndicator component.
分页符组件MobilePageIndicator

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- color (a value equal to: 'primary', 'white'; default 'primary'):
    用于设置当前分页符预设颜色方案  可选的有'primary'、'white'  默认：'primary'.

- current (number; optional):
    用于设置当前分页符所在的页下标（从0开始计数）.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于设置当前分页符显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'.

- total (number; optional):
    用于设置当前分页符总页数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePageIndicator'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        color: typing.Optional[Literal["primary", "white"]] = None,
        current: typing.Optional[NumberType] = None,
        direction: typing.Optional[Literal["horizontal", "vertical"]] = None,
        total: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'color', 'current', 'direction', 'total']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'color', 'current', 'direction', 'total']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobilePageIndicator, self).__init__(**args)

setattr(MobilePageIndicator, "__init__", _explicitize_args(MobilePageIndicator.__init__))
