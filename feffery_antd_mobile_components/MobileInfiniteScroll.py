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


class MobileInfiniteScroll(Component):
    """A MobileInfiniteScroll component.
无限滚动组件MobileInfiniteScroll

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- threshold (number; default 250):
    触发刷新对应的滚动触底像素距离阈值  默认值：`250`.

- refreshCount (number; default 0):
    监听滚动到底部操作累计触发次数  默认值：`0`.

- stopRefreshing (boolean; optional):
    用于手动终止进行中的加载过程，每次调用会将更新为`True`后，都会在终止加载状态后，被重置为`False`.

- hasMore (boolean; default True):
    控制是否可继续滚动触底触发新的加载  默认值：`True`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileInfiniteScroll'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        threshold: typing.Optional[NumberType] = None,
        refreshCount: typing.Optional[NumberType] = None,
        stopRefreshing: typing.Optional[bool] = None,
        hasMore: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'threshold', 'refreshCount', 'stopRefreshing', 'hasMore']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'threshold', 'refreshCount', 'stopRefreshing', 'hasMore']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileInfiniteScroll, self).__init__(**args)

setattr(MobileInfiniteScroll, "__init__", _explicitize_args(MobileInfiniteScroll.__init__))
