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


class MobileCheckbox(Component):
    """A MobileCheckbox component.
复选框组件MobileCheckbox

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置当前复选框标签内容.

- block (boolean; default False):
    是否撑满父级元素  默认：False.

- checked (boolean; default False):
    设置或监听当前复选框是否选中  默认：False.

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- icon (dict; optional):
    自定义各状态下的图标元素.

    `icon` is a dict with keys:

    - checked (a list of or a singular dash component, string or number; optional):
        自定义选中状态下图标元素.

    - unchecked (a list of or a singular dash component, string or number; optional):
        自定义非选中状态下图标元素.

    - indeterminate (a list of or a singular dash component, string or number; optional):
        自定义半选中状态下图标元素.

- indeterminate (boolean; default False):
    是否以半选中状态进行渲染，仅用作样式控制."""
    _children_props = ['icon.checked', 'icon.unchecked', 'icon.indeterminate']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckbox'
    Icon = TypedDict(
        "Icon",
            {
            "checked": NotRequired[ComponentType],
            "unchecked": NotRequired[ComponentType],
            "indeterminate": NotRequired[ComponentType]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        block: typing.Optional[bool] = None,
        checked: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        icon: typing.Optional["Icon"] = None,
        indeterminate: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'block', 'checked', 'disabled', 'icon', 'indeterminate']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'block', 'checked', 'disabled', 'icon', 'indeterminate']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCheckbox, self).__init__(children=children, **args)

setattr(MobileCheckbox, "__init__", _explicitize_args(MobileCheckbox.__init__))
