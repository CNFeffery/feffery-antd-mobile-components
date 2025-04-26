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


class MobileTag(Component):
    """A MobileTag component.
标签组件MobileTag

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- color (a value equal to: 'default', 'primary', 'success', 'warning', 'danger' | string; default 'default'):
    用于为当前标签设置颜色
    内置的状态色有'default'、'primary'、'success'、'warning'、'danger'
    也可传入css中合法的色彩值作为自定义颜色  默认：'default'.

- fill (a value equal to: 'solid', 'outline'; default 'solid'):
    用于为当前标签设置填充模式  可选的有'solid'、'outline'  默认：'solid'.

- round (boolean; default False):
    用于为当前标签设置是否开启圆角  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileTag'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        color: typing.Optional[typing.Union[Literal["default", "primary", "success", "warning", "danger"], str]] = None,
        fill: typing.Optional[Literal["solid", "outline"]] = None,
        round: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'color', 'fill', 'round']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'color', 'fill', 'round']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileTag, self).__init__(children=children, **args)

setattr(MobileTag, "__init__", _explicitize_args(MobileTag.__init__))
