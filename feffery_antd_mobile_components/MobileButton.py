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


class MobileButton(Component):
    """A MobileButton component.
按钮组件MobileButton

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- block (boolean; default False):
    当前按钮是否撑满父元素  默认值：`False`.

- color (a value equal to: 'default', 'primary', 'success', 'warning', 'danger'; default 'default'):
    按钮颜色状态，可选项有`'default'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
    默认值：`'default'`.

- disabled (boolean; default False):
    是否禁用当前按钮  默认值：`False`.

- fill (a value equal to: 'solid', 'outline', 'none'; default 'solid'):
    当前按钮填充模式，可选项有`'solid'`、`'outline'`、`'none'`  默认值：`'solid'`.

- loading (boolean; default False):
    当前按钮是否处于加载中状态  默认值：`False`.

- loadingText (string; optional):
    加载中状态下额外展示的文字内容.

- shape (a value equal to: 'default', 'rounded', 'rectangular'; default 'default'):
    用于设置当前按钮的形状，可选项有`'default'`、`'rounded'`、`'rectangular'`
    默认值：`'default'`.

- size (a value equal to: 'mini', 'small', 'middle', 'large'; default 'middle'):
    用于设置当前按钮的尺寸规格，可选项有`'mini'`、`'small'`、`'middle'`、`'large'`
    默认值：`'middle'`.

- type (a value equal to: 'submit', 'reset', 'button'; default 'button'):
    用于设置当前按钮对应原生`html`的`type`属性，可选项有`'submit'`、`'reset'`、`'button'`
    默认值：`'button'`.

- nClicks (number; default 0):
    监听当前按钮累计被点击次数  默认值：`0`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        block: typing.Optional[bool] = None,
        color: typing.Optional[Literal["default", "primary", "success", "warning", "danger"]] = None,
        disabled: typing.Optional[bool] = None,
        fill: typing.Optional[Literal["solid", "outline", "none"]] = None,
        loading: typing.Optional[bool] = None,
        loadingText: typing.Optional[str] = None,
        shape: typing.Optional[Literal["default", "rounded", "rectangular"]] = None,
        size: typing.Optional[Literal["mini", "small", "middle", "large"]] = None,
        type: typing.Optional[Literal["submit", "reset", "button"]] = None,
        nClicks: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'block', 'color', 'disabled', 'fill', 'loading', 'loadingText', 'shape', 'size', 'type', 'nClicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'block', 'color', 'disabled', 'fill', 'loading', 'loadingText', 'shape', 'size', 'type', 'nClicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileButton, self).__init__(children=children, **args)

setattr(MobileButton, "__init__", _explicitize_args(MobileButton.__init__))
