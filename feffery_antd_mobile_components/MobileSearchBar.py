# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileSearchBar(Component):
    """A MobileSearchBar component.
搜索框组件MobileSearchBar

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- cancelText (string; default '取消'):
    取消按钮文案  默认：'取消'.

- clearOnCancel (boolean; default True):
    点击取消按钮后是否清空已输入内容  默认：True.

- clearable (boolean; default True):
    是否渲染取消按钮  默认：True.

- icon (a list of or a singular dash component, string or number; optional):
    自定义前缀图标.

- maxLength (number; optional):
    限制允许输入内容的长度上限  默认无限制.

- onlyShowClearWhenFocus (boolean; default False):
    是否仅在当前搜索框聚焦时才显示取消按钮  默认：False.

- placeholder (string; optional):
    提示文本内容.

- showCancelButton (boolean; default False):
    是否在搜索框右侧显示取消按钮  默认：False.

- value (string; optional):
    设置或监听当前搜索框内的已输入文字内容.

- debounceValue (string; optional):
    value的防抖状态值.

- debounceWait (number; default 200):
    针对debounceValue的防抖延时，单位：毫秒  默认：200."""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSearchBar'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        cancelText: typing.Optional[str] = None,
        clearOnCancel: typing.Optional[bool] = None,
        clearable: typing.Optional[bool] = None,
        icon: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        maxLength: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        onlyShowClearWhenFocus: typing.Optional[bool] = None,
        placeholder: typing.Optional[str] = None,
        showCancelButton: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        debounceValue: typing.Optional[str] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'cancelText', 'clearOnCancel', 'clearable', 'icon', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'showCancelButton', 'value', 'debounceValue', 'debounceWait']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'cancelText', 'clearOnCancel', 'clearable', 'icon', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'showCancelButton', 'value', 'debounceValue', 'debounceWait']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSearchBar, self).__init__(**args)
