# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileToast(Component):
    """A MobileToast component.
轻提示组件MobileToast

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- content (a list of or a singular dash component, string or number; optional):
    轻提示内容.

- duration (number; default 2000):
    持续显示时长，单位：毫秒  默认：2000.

- icon (a value equal to: 'success', 'fail', 'loading'; optional):
    额外图标类型，可选的有'success'、'fail'、'loading'.

- maskClassName (string; optional):
    遮罩层css类名.

- maskClickable (boolean; default True):
    背景是否可点击  默认：True.

- maskStyle (dict; optional):
    遮罩层css样式.

- position (a value equal to: 'top', 'bottom', 'center'; default 'center'):
    垂直方向显示位置，可选的有'top'、'bottom'、'center'  默认：'center'."""
    _children_props = ['content']
    _base_nodes = ['content', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileToast'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        content: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        duration: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        icon: typing.Optional[Literal["success", "fail", "loading"]] = None,
        maskClassName: typing.Optional[str] = None,
        maskClickable: typing.Optional[bool] = None,
        maskStyle: typing.Optional[dict] = None,
        position: typing.Optional[Literal["top", "bottom", "center"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'content', 'duration', 'icon', 'maskClassName', 'maskClickable', 'maskStyle', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'content', 'duration', 'icon', 'maskClassName', 'maskClickable', 'maskStyle', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileToast, self).__init__(**args)
