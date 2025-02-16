# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileInput(Component):
    """A MobileInput component.
输入框组件MobileInput

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- type (a value equal to: 'text', 'password'; default 'text'):
    用于设置当前输入框的类型  可选的有'text'、'password'  默认：'text'.

- clearable (boolean; default False):
    是否渲染清除按钮  默认：False.

- defaultValue (string; optional):
    设置初始化已输入内容.

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- maxLength (number; optional):
    限制允许输入内容的长度上限  默认无限制.

- onlyShowClearWhenFocus (boolean; default True):
    是否仅在当前输入框聚焦时才显示取消按钮  默认：True.

- placeholder (string; optional):
    提示文本内容.

- readOnly (boolean; default False):
    用于设置是否以只读模式渲染当前组件  默认：False.

- value (string; optional):
    设置或监听当前输入框内的已输入文字内容.

- debounceValue (string; optional):
    value的防抖状态值.

- debounceWait (number; default 200):
    针对debounceValue的防抖延时，单位：毫秒  默认：200."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileInput'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        type: typing.Optional[Literal["text", "password"]] = None,
        clearable: typing.Optional[bool] = None,
        defaultValue: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        maxLength: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        onlyShowClearWhenFocus: typing.Optional[bool] = None,
        placeholder: typing.Optional[str] = None,
        readOnly: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        debounceValue: typing.Optional[str] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'type', 'clearable', 'defaultValue', 'disabled', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'readOnly', 'value', 'debounceValue', 'debounceWait']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'type', 'clearable', 'defaultValue', 'disabled', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'readOnly', 'value', 'debounceValue', 'debounceWait']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileInput, self).__init__(**args)
