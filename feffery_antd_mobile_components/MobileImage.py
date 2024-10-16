# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileImage(Component):
    """A MobileImage component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

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
    用于记录当前图片累计被点击次数.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['fallback']
    _base_nodes = ['fallback', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileImage'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, alt=Component.UNDEFINED, draggable=Component.UNDEFINED, fallback=Component.UNDEFINED, fit=Component.UNDEFINED, height=Component.UNDEFINED, lazy=Component.UNDEFINED, src=Component.UNDEFINED, width=Component.UNDEFINED, nClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'alt', 'draggable', 'fallback', 'fit', 'height', 'lazy', 'src', 'width', 'nClicks', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'alt', 'draggable', 'fallback', 'fit', 'height', 'lazy', 'src', 'width', 'nClicks', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileImage, self).__init__(**args)
