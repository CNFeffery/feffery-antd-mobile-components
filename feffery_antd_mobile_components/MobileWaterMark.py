# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileWaterMark(Component):
    """A MobileWaterMark component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

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

- key (string; optional):
    强制重绘当前组件时使用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- rotate (number; default -22):
    用于设置水印图片旋转角度  默认：-22.

- style (dict; optional):
    用于为当前组件设置css样式.

- width (number; default 120):
    用于设置水印像素宽度  默认：120.

- zIndex (number; default 2000):
    用于设置水印元素的z-index属性  默认：2000."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileWaterMark'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, content=Component.UNDEFINED, fontColor=Component.UNDEFINED, fontSize=Component.UNDEFINED, fullPage=Component.UNDEFINED, gapX=Component.UNDEFINED, gapY=Component.UNDEFINED, height=Component.UNDEFINED, image=Component.UNDEFINED, imageHeight=Component.UNDEFINED, imageWidth=Component.UNDEFINED, rotate=Component.UNDEFINED, width=Component.UNDEFINED, zIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'content', 'fontColor', 'fontSize', 'fullPage', 'gapX', 'gapY', 'height', 'image', 'imageHeight', 'imageWidth', 'key', 'loading_state', 'rotate', 'style', 'width', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'content', 'fontColor', 'fontSize', 'fullPage', 'gapX', 'gapY', 'height', 'image', 'imageHeight', 'imageWidth', 'key', 'loading_state', 'rotate', 'style', 'width', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileWaterMark, self).__init__(**args)
