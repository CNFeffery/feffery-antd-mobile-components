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


class MobileImage(Component):
    """A MobileImage component.
图片组件MobileImage

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- alt (string; optional):
    用于设置当前图片的描述文字.

- draggable (boolean; default False):
    用于设置当前图片是否可拖拽  默认：False.

- fallback (a list of or a singular dash component, string or number; optional):
    用于为当前图片组件设置加载失败时的占位图.

- fit (a value equal to: 'contain', 'cover', 'fill', 'none', 'scale-down'; default 'fill'):
    用于设置当前图片的填充模式  可选的有'contain'、'cover'、'fill'、'none'、'scale-down'
    默认：'fill'.

- height (number | string; optional):
    用于设置当前图片的高度  当传入数值型时会被视作像素高度.

- lazy (boolean; default False):
    用于设置当前图片是否开启懒加载功能  默认：False.

- src (string; optional):
    用于设置当前图片资源地址.

- width (number | string; optional):
    用于设置当前图片的宽度  当传入数值型时会被视作像素宽度.

- nClicks (number; default 0):
    用于记录当前图片累计被点击次数."""
    _children_props = ['fallback']
    _base_nodes = ['fallback', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileImage'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        alt: typing.Optional[str] = None,
        draggable: typing.Optional[bool] = None,
        fallback: typing.Optional[ComponentType] = None,
        fit: typing.Optional[Literal["contain", "cover", "fill", "none", "scale-down"]] = None,
        height: typing.Optional[typing.Union[NumberType, str]] = None,
        lazy: typing.Optional[bool] = None,
        src: typing.Optional[str] = None,
        width: typing.Optional[typing.Union[NumberType, str]] = None,
        nClicks: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'alt', 'draggable', 'fallback', 'fit', 'height', 'lazy', 'src', 'width', 'nClicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'alt', 'draggable', 'fallback', 'fit', 'height', 'lazy', 'src', 'width', 'nClicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileImage, self).__init__(**args)

setattr(MobileImage, "__init__", _explicitize_args(MobileImage.__init__))
