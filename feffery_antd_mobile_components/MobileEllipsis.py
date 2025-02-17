# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileEllipsis(Component):
    """A MobileEllipsis component.
文本省略组件MobileEllipsis

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- collapseText (a list of or a singular dash component, string or number; default ''):
    用于设置收起操作文案内容  默认：''.

- content (string; optional):
    用于设置文字内容.

- direction (a value equal to: 'start', 'end', 'middle'; default 'end'):
    用于设置省略位置，可选的有'start'、'end'、'middle'  默认：'end'.

- expandText (a list of or a singular dash component, string or number; optional):
    用于设置展开操作文案内容.

- rows (number; default 1):
    用于设置展示文字内容的行数  默认：1.

- defaultExpanded (boolean; default False):
    用于设置初始化时候展开  默认：False."""
    _children_props = ['collapseText', 'expandText']
    _base_nodes = ['collapseText', 'expandText', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileEllipsis'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        collapseText: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        content: typing.Optional[str] = None,
        direction: typing.Optional[Literal["start", "end", "middle"]] = None,
        expandText: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        rows: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        defaultExpanded: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'collapseText', 'content', 'direction', 'expandText', 'rows', 'defaultExpanded']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'collapseText', 'content', 'direction', 'expandText', 'rows', 'defaultExpanded']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileEllipsis, self).__init__(**args)
