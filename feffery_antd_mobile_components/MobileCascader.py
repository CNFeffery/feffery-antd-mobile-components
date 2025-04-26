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


class MobileCascader(Component):
    """A MobileCascader component.
级联选择组件MobileCascader

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- cancelText (string; default '取消'):
    用于为当前级联选择设置取消按钮文案信息  默认：'取消'.

- confirmText (string; default '确认'):
    用于为当前级联选择设置确认按钮文案信息  默认：'确认'.

- defaultValue (list of strings; optional):
    用于为当前级联选择设置默认选中项.

- destroyOnClose (boolean; default True):
    当前级联选择组件不可见时是否进行销毁  默认：True.

- forceRender (boolean; default False):
    用于设置初始化时是否强制渲染当前级联选择组件  默认：False.

- options (optional):
    用于为当前级联选择组件配置级联选项数据  默认：[].

- placeholder (string; default '请选择'):
    用于为当前级联选择设置无选中项时的提示文字  默认：'请选择'.

- title (string | a list of or a singular dash component, string or number; optional):
    为当前级联选择设置标题内容.

- value (list of strings; optional):
    用于设置或监听当前已选中项.

- visible (boolean; default False):
    用于设置是否显示当前级联选择  默认：False."""
    _children_props = ['title']
    _base_nodes = ['title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCascader'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        cancelText: typing.Optional[str] = None,
        confirmText: typing.Optional[str] = None,
        defaultValue: typing.Optional[typing.Sequence[str]] = None,
        destroyOnClose: typing.Optional[bool] = None,
        forceRender: typing.Optional[bool] = None,
        options: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[str] = None,
        title: typing.Optional[typing.Union[str, ComponentType]] = None,
        value: typing.Optional[typing.Sequence[str]] = None,
        visible: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'cancelText', 'confirmText', 'defaultValue', 'destroyOnClose', 'forceRender', 'options', 'placeholder', 'title', 'value', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'cancelText', 'confirmText', 'defaultValue', 'destroyOnClose', 'forceRender', 'options', 'placeholder', 'title', 'value', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCascader, self).__init__(**args)

setattr(MobileCascader, "__init__", _explicitize_args(MobileCascader.__init__))
