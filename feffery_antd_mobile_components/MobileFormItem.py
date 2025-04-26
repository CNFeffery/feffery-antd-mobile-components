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


class MobileFormItem(Component):
    """A MobileFormItem component.
表单项组件MobileFormItem

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于传入内部各MobileFormItem表单项组件.

- childElementPosition (a value equal to: 'normal', 'right'; default 'normal'):
    表单项控件的位置，可选的有'normal'、'right'  默认：'normal'.

- disabled (boolean; optional):
    是否禁用当前组件  默认：False.

- help (a list of or a singular dash component, string or number; optional):
    额外提示信息.

- hidden (boolean; default False):
    是否隐藏当前表单项  默认：False.

- label (a list of or a singular dash component, string or number; optional):
    标签内容.

- layout (a value equal to: 'vertical', 'horizontal'; optional):
    自定义布局模式，可选的有'vertical'、'horizontal'  默认以父级表单组件的布局模式为准.

- required (boolean; default False):
    是否显示必选标记  默认：False."""
    _children_props = ['help', 'label']
    _base_nodes = ['help', 'label', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileFormItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        childElementPosition: typing.Optional[Literal["normal", "right"]] = None,
        disabled: typing.Optional[bool] = None,
        help: typing.Optional[ComponentType] = None,
        hidden: typing.Optional[bool] = None,
        label: typing.Optional[ComponentType] = None,
        layout: typing.Optional[Literal["vertical", "horizontal"]] = None,
        required: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'childElementPosition', 'disabled', 'help', 'hidden', 'label', 'layout', 'required']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'childElementPosition', 'disabled', 'help', 'hidden', 'label', 'layout', 'required']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileFormItem, self).__init__(children=children, **args)

setattr(MobileFormItem, "__init__", _explicitize_args(MobileFormItem.__init__))
