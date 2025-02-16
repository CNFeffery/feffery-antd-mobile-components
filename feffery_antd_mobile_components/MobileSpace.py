# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileSpace(Component):
    """A MobileSpace component.
间距组件MobileSpace

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
    用于设置内部元素.

- align (a value equal to: 'start', 'end', 'center', 'baseline'; optional):
    用于设置当前间距组件的交叉轴对齐方式  可选的有'start'、'end'、'center'、'baseline'.

- block (boolean; default False):
    用于设置当前间距组件是否撑满父元素  默认：False.

- direction (a value equal to: 'vertical', 'horizontal'; default 'horizontal'):
    用于设置当前间距组件的方向  可选的有'vertical'、'horizontal'  默认：'horizontal'.

- justify (a value equal to: 'start', 'end', 'center', 'between', 'around', 'evenly', 'stretch'; optional):
    用于设置当前间距组件的主轴对齐方式
    可选的有'start'、'end'、'center'、'between'、'around'、'evenly'、'stretch'.

- wrap (boolean; default False):
    用于设置当前间距组件是否自动换行，仅在'horizontal'方向下有效  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSpace'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        align: typing.Optional[Literal["start", "end", "center", "baseline"]] = None,
        block: typing.Optional[bool] = None,
        direction: typing.Optional[Literal["vertical", "horizontal"]] = None,
        justify: typing.Optional[Literal["start", "end", "center", "between", "around", "evenly", "stretch"]] = None,
        wrap: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'align', 'block', 'direction', 'justify', 'wrap']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'align', 'block', 'direction', 'justify', 'wrap']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileSpace, self).__init__(children=children, **args)
