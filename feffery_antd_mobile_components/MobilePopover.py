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


class MobilePopover(Component):
    """A MobilePopover component.
气泡弹出框组件MobilePopover

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置触发目标元素.

- content (a list of or a singular dash component, string or number; optional):
    设置气泡框内部元素.

- destroyOnHide (boolean; default False):
    隐藏时，是否销毁气泡框内部元素  默认：False.

- mode (a value equal to: 'light', 'dark'; default 'light'):
    设置显示模式，可选的有'light'、'dark'  默认：'light'.

- placement (a value equal to: 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; default 'top'):
    设置气泡框位置，可选的有'top'、'top-start'、'top-end'、'right'、'right-start'、'right-end'、'bottom'、'bottom-start'
    、'bottom-end'、'left'、'left-start'、'left-end'  默认：'top'.

- visible (boolean; optional):
    监听或设置当前气泡框是否处于展开状态."""
    _children_props = ['content']
    _base_nodes = ['content', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePopover'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        content: typing.Optional[ComponentType] = None,
        destroyOnHide: typing.Optional[bool] = None,
        mode: typing.Optional[Literal["light", "dark"]] = None,
        placement: typing.Optional[Literal["top", "top-start", "top-end", "right", "right-start", "right-end", "bottom", "bottom-start", "bottom-end", "left", "left-start", "left-end"]] = None,
        visible: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'content', 'destroyOnHide', 'mode', 'placement', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'content', 'destroyOnHide', 'mode', 'placement', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobilePopover, self).__init__(children=children, **args)

setattr(MobilePopover, "__init__", _explicitize_args(MobilePopover.__init__))
