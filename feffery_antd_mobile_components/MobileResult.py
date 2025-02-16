# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileResult(Component):
    """A MobileResult component.
结果组件MobileResult

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- description (a list of or a singular dash component, string or number; optional):
    描述信息.

- icon (a list of or a singular dash component, string or number; optional):
    自定义图标.

- status (a value equal to: 'success', 'error', 'info', 'waiting', 'warning'; default 'info'):
    状态类型，可选的有'success'、'error'、'info'、'waiting'、'warning'  默认：'info'.

- title (a list of or a singular dash component, string or number; optional):
    标题信息."""
    _children_props = ['description', 'icon', 'title']
    _base_nodes = ['description', 'icon', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileResult'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        description: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        icon: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        status: typing.Optional[Literal["success", "error", "info", "waiting", "warning"]] = None,
        title: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'description', 'icon', 'status', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'description', 'icon', 'status', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileResult, self).__init__(**args)
