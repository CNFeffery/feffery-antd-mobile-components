# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileImageViewer(Component):
    """A MobileImageViewer component.
图片查看器组件MobileImageViewer

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- mode (a value equal to: 'default', 'multiple'; default 'default'):
    用于设置当前图片查看器的显示模式  可选的有'default'、'multiple'，分别对应参数image、images
    默认：'default'.

- defaultIndex (number; default 0):
    当mode='multiple'时，用于设置默认显示的图片位序  默认：0.

- image (string; optional):
    当mode='default'时，用于设置目标图片资源地址.

- images (list of strings; optional):
    当mode='multiple'时，用于设置目标图片资源地址数组.

- maxZoom (number | a value equal to: 'auto'; default 3):
    设置图片查看时的最大缩放倍数  默认：3.

- visible (boolean; default False):
    用于监听或设置当前图片查看器是否处于显示状态  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileImageViewer'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        mode: typing.Optional[Literal["default", "multiple"]] = None,
        defaultIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        image: typing.Optional[str] = None,
        images: typing.Optional[typing.Sequence[str]] = None,
        maxZoom: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], Literal["auto"]]] = None,
        visible: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'mode', 'defaultIndex', 'image', 'images', 'maxZoom', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'mode', 'defaultIndex', 'image', 'images', 'maxZoom', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileImageViewer, self).__init__(**args)
