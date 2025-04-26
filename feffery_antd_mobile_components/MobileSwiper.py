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


class MobileSwiper(Component):
    """A MobileSwiper component.
走马灯组件MobileSwiper

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- items (list of dicts; optional):
    用于定义内部各子项.

    `items` is a list of dicts with keys:

    - key (string; required):
        必填，用于为当前子项设置唯一识别id.

    - children (a list of or a singular dash component, string or number; optional):
        用于为当前子项设置内部元素.

- allowTouchMove (boolean; default True):
    用于为当前走马灯组件设置是否允许手势滑动  默认：True.

- autoplay (boolean; default False):
    用于为当前走马灯组件设置是否自动切换  默认：False.

- autoplayInterval (number; default 3000):
    用于为当前走马灯组件设置自动切换时间间隔，单位：毫秒  默认：3000.

- defaultIndex (number; default 0):
    用于为当前走马灯设置初始展示的子项位序（从0开始计数）  默认：0.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于为当前走马灯设置显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'.

- loop (boolean; default False):
    用于为当前走马灯设置是否循环轮播  默认：False.

- rubberband (boolean; default True):
    用于为当前走马灯设置是否在拖动超出内容区域时启用橡皮筋效果  仅在非loop模式下可用  默认：True.

- slideSize (number; default 100):
    用于为当前走马灯设置滑块的宽度百分比  默认：100.

- stuckAtBoundary (boolean; default True):
    用于为当前走马灯设置是否在边界两边卡住，避免出现空白  仅在非loop模式下且slideSize<100时生效  默认：True.

- trackOffset (number; default 0):
    用于为当前走马灯设置滑块轨道整体的偏移量百分比  默认：0."""
    _children_props = ['items[].children']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSwiper'
    Items = TypedDict(
        "Items",
            {
            "key": str,
            "children": NotRequired[ComponentType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        items: typing.Optional[typing.Sequence["Items"]] = None,
        allowTouchMove: typing.Optional[bool] = None,
        autoplay: typing.Optional[bool] = None,
        autoplayInterval: typing.Optional[NumberType] = None,
        defaultIndex: typing.Optional[NumberType] = None,
        direction: typing.Optional[Literal["horizontal", "vertical"]] = None,
        loop: typing.Optional[bool] = None,
        rubberband: typing.Optional[bool] = None,
        slideSize: typing.Optional[NumberType] = None,
        stuckAtBoundary: typing.Optional[bool] = None,
        trackOffset: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'items', 'allowTouchMove', 'autoplay', 'autoplayInterval', 'defaultIndex', 'direction', 'loop', 'rubberband', 'slideSize', 'stuckAtBoundary', 'trackOffset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'items', 'allowTouchMove', 'autoplay', 'autoplayInterval', 'defaultIndex', 'direction', 'loop', 'rubberband', 'slideSize', 'stuckAtBoundary', 'trackOffset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSwiper, self).__init__(**args)

setattr(MobileSwiper, "__init__", _explicitize_args(MobileSwiper.__init__))
