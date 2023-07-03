# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileSwiper(Component):
    """A MobileSwiper component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- allowTouchMove (boolean; default True):
    用于为当前走马灯组件设置是否允许手势滑动  默认：True.

- autoplay (boolean; default False):
    用于为当前走马灯组件设置是否自动切换  默认：False.

- autoplayInterval (number; default 3000):
    用于为当前走马灯组件设置自动切换时间间隔，单位：毫秒  默认：3000.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultIndex (number; default 0):
    用于为当前走马灯设置初始展示的子项位序（从0开始计数）  默认：0.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于为当前走马灯设置显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'.

- items (list of dicts; optional):
    用于定义内部各子项.

    `items` is a list of dicts with keys:

    - children (a list of or a singular dash component, string or number; optional):
        用于为当前子项设置内部元素.

    - key (string; required):
        必填，用于为当前子项设置唯一识别id.

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

- loop (boolean; default False):
    用于为当前走马灯设置是否循环轮播  默认：False.

- rubberband (boolean; default True):
    用于为当前走马灯设置是否在拖动超出内容区域时启用橡皮筋效果  仅在非loop模式下可用  默认：True.

- slideSize (number; default 100):
    用于为当前走马灯设置滑块的宽度百分比  默认：100.

- stuckAtBoundary (boolean; default True):
    用于为当前走马灯设置是否在边界两边卡住，避免出现空白  仅在非loop模式下且slideSize<100时生效  默认：True.

- style (dict; optional):
    用于为当前组件设置css样式.

- trackOffset (number; default 0):
    用于为当前走马灯设置滑块轨道整体的偏移量百分比  默认：0."""
    _children_props = ['items[].children']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSwiper'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, items=Component.UNDEFINED, allowTouchMove=Component.UNDEFINED, autoplay=Component.UNDEFINED, autoplayInterval=Component.UNDEFINED, defaultIndex=Component.UNDEFINED, direction=Component.UNDEFINED, loop=Component.UNDEFINED, rubberband=Component.UNDEFINED, slideSize=Component.UNDEFINED, stuckAtBoundary=Component.UNDEFINED, trackOffset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowTouchMove', 'autoplay', 'autoplayInterval', 'className', 'defaultIndex', 'direction', 'items', 'key', 'loading_state', 'loop', 'rubberband', 'slideSize', 'stuckAtBoundary', 'style', 'trackOffset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowTouchMove', 'autoplay', 'autoplayInterval', 'className', 'defaultIndex', 'direction', 'items', 'key', 'loading_state', 'loop', 'rubberband', 'slideSize', 'stuckAtBoundary', 'style', 'trackOffset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSwiper, self).__init__(**args)
