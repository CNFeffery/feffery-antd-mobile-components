# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileWaterMark(Component):
    """A MobileWaterMark component.
水印组件MobileWaterMark

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- content (string | list of strings; optional):
    用于设置水印文字内容，当传入数组时用于表示多行文字.

- fontColor (string; default 'rgba(0, 0, 0, .15)'):
    用于设置水印文字颜色  默认：'rgba(0, 0, 0, .15)'.

- fontSize (number | string; default 14):
    用于设置水印文字大小  默认：14.

- fullPage (boolean; default True):
    用于设置水印是否覆盖整个页面  默认：True.

- gapX (number; default 24):
    用于设置水印之间的水平像素间距  默认：24.

- gapY (number; default 48):
    用于设置水印之间的垂直像素间距  默认：48.

- height (number; default 64):
    用于设置水印像素高度  默认：64.

- image (string; optional):
    用于设置水印图片地址，当image与content同时设置时，优先使用图片水印.

- imageHeight (number; default 64):
    用于设置水印图片像素高度  默认：64.

- imageWidth (number; default 120):
    用于设置水印图片像素宽度  默认：120.

- rotate (number; default -22):
    用于设置水印图片旋转角度  默认：-22.

- width (number; default 120):
    用于设置水印像素宽度  默认：120.

- zIndex (number; default 2000):
    用于设置水印元素的z-index属性  默认：2000."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileWaterMark'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        content: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fontColor: typing.Optional[str] = None,
        fontSize: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], str]] = None,
        fullPage: typing.Optional[bool] = None,
        gapX: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        gapY: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        image: typing.Optional[str] = None,
        imageHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        imageWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        rotate: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        zIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'content', 'fontColor', 'fontSize', 'fullPage', 'gapX', 'gapY', 'height', 'image', 'imageHeight', 'imageWidth', 'rotate', 'width', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'content', 'fontColor', 'fontSize', 'fullPage', 'gapX', 'gapY', 'height', 'image', 'imageHeight', 'imageWidth', 'rotate', 'width', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileWaterMark, self).__init__(**args)
