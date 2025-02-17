# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileFloatingBubble(Component):
    """A MobileFloatingBubble component.
浮动气泡组件MobileFloatingBubble

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

- axis (a value equal to: 'xy', 'lock', 'x', 'y'; default 'y'):
    设置可进行拖动的方向，可选的有'xy'（自由拖动）、'lock'（仅允许在开始拖拽时的方向上进行拖拽）、'x'（仅允许在水平方向上进行拖拽）、'y'（仅允许在垂直方向上进行拖拽）
    默认：'y'.

- magnetic (a value equal to: 'x', 'y'; optional):
    设置自动磁吸的方向，可选的有'x'、'y'，默认不开启磁吸效果.

- offset (dict; optional):
    监听或设置像素偏移位置.

    `offset` is a dict with keys:

    - x (number; optional):
        水平方向像素偏移位置  默认：0.

    - y (number; optional):
        垂直方向像素偏移位置  默认：0.

- nClicks (number; default 0):
    监听当前浮动气泡组件累计被点击次数  默认：0."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileFloatingBubble'
    Offset = TypedDict(
        "Offset",
            {
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        axis: typing.Optional[Literal["xy", "lock", "x", "y"]] = None,
        magnetic: typing.Optional[Literal["x", "y"]] = None,
        offset: typing.Optional["Offset"] = None,
        nClicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'axis', 'magnetic', 'offset', 'nClicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'axis', 'magnetic', 'offset', 'nClicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileFloatingBubble, self).__init__(children=children, **args)
