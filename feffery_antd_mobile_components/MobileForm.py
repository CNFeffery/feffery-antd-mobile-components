# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileForm(Component):
    """A MobileForm component.
表单组件MobileForm

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于传入内部各MobileFormItem表单项组件.

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- footer (a list of or a singular dash component, string or number; optional):
    自定义表单底部元素.

- layout (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    布局模式，可选的有'vertical'、'horizontal'  默认：'vertical'.

- mode (a value equal to: 'default', 'card'; default 'default'):
    渲染模式，可选的有'default'、'card'  默认：'default'.

- requiredMarkStyle (a value equal to: 'asterisk', 'text-required', 'text-optional', 'none'; default 'asterisk'):
    针对内部表单项的必填选填标记样式类型进行设置
    可选的有'asterisk'、'text-required'、'text-optional'、'none'
    默认：'asterisk'."""
    _children_props = ['footer']
    _base_nodes = ['footer', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileForm'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        footer: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        layout: typing.Optional[Literal["vertical", "horizontal"]] = None,
        mode: typing.Optional[Literal["default", "card"]] = None,
        requiredMarkStyle: typing.Optional[Literal["asterisk", "text-required", "text-optional", "none"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'disabled', 'footer', 'layout', 'mode', 'requiredMarkStyle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'disabled', 'footer', 'layout', 'mode', 'requiredMarkStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileForm, self).__init__(children=children, **args)
