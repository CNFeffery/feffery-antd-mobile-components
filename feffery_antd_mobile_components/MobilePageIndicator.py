# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobilePageIndicator(Component):
    """A MobilePageIndicator component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- color (a value equal to: 'primary', 'white'; default 'primary'):
    用于设置当前分页符预设颜色方案  可选的有'primary'、'white'  默认：'primary'.

- current (number; optional):
    用于设置当前分页符所在的页下标（从0开始计数）.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于设置当前分页符显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'.

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

- style (dict; optional):
    用于为当前组件设置css样式.

- total (number; optional):
    用于设置当前分页符总页数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePageIndicator'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, current=Component.UNDEFINED, direction=Component.UNDEFINED, total=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'color', 'current', 'direction', 'key', 'loading_state', 'style', 'total']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'current', 'direction', 'key', 'loading_state', 'style', 'total']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobilePageIndicator, self).__init__(**args)
