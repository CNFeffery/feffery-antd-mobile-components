# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileFloatingBubble(Component):
    """A MobileFloatingBubble component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- axis (a value equal to: 'xy', 'lock', 'x', 'y'; default 'y'):
    设置可进行拖动的方向，可选的有'xy'（自由拖动）、'lock'（仅允许在开始拖拽时的方向上进行拖拽）、'x'（仅允许在水平方向上进行拖拽）、'y'（仅允许在垂直方向上进行拖拽）
    默认：'y'.

- className (string; optional):
    用于为当前组件设置css类名.

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

- magnetic (a value equal to: 'x', 'y'; optional):
    设置自动磁吸的方向，可选的有'x'、'y'，默认不开启磁吸效果.

- nClicks (number; default 0):
    监听当前浮动气泡组件累计被点击次数  默认：0.

- offset (dict; optional):
    监听或设置像素偏移位置.

    `offset` is a dict with keys:

    - x (number; optional):
        水平方向像素偏移位置  默认：0.

    - y (number; optional):
        垂直方向像素偏移位置  默认：0.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileFloatingBubble'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, axis=Component.UNDEFINED, magnetic=Component.UNDEFINED, offset=Component.UNDEFINED, nClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'axis', 'className', 'key', 'loading_state', 'magnetic', 'nClicks', 'offset', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'axis', 'className', 'key', 'loading_state', 'magnetic', 'nClicks', 'offset', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileFloatingBubble, self).__init__(children=children, **args)
