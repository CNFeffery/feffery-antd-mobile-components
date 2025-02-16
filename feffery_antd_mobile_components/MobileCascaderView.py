# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileCascaderView(Component):
    """A MobileCascaderView component.
级联选择视图组件MobileCascaderView

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultValue (list of strings; optional):
    用于为当前级联选择视图设置默认选中项.

- options (optional):
    用于为当前级联选择视图组件配置级联选项数据  默认：[].

- placeholder (string; default '请选择'):
    用于为当前级联选择视图设置无选中项时的提示文字  默认：'请选择'.

- value (list of strings; optional):
    用于设置或监听当前已选中项.

- loading (boolean; default False):
    用于为当前级联选择视图组件设置是否开启加载中状态  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCascaderView'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        defaultValue: typing.Optional[typing.Sequence[str]] = None,
        options: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[str] = None,
        value: typing.Optional[typing.Sequence[str]] = None,
        loading: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'defaultValue', 'options', 'placeholder', 'value', 'loading']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'defaultValue', 'options', 'placeholder', 'value', 'loading']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCascaderView, self).__init__(**args)
