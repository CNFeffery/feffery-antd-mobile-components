# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileTag(Component):
    """A MobileTag component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- color (a value equal to: 'default', 'primary', 'success', 'warning', 'danger' | string; default 'default'):
    用于为当前标签设置颜色
    内置的状态色有'default'、'primary'、'success'、'warning'、'danger'
    也可传入css中合法的色彩值作为自定义颜色  默认：'default'.

- fill (a value equal to: 'solid', 'outline'; default 'solid'):
    用于为当前标签设置填充模式  可选的有'solid'、'outline'  默认：'solid'.

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

- round (boolean; default False):
    用于为当前标签设置是否开启圆角  默认：False.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileTag'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, fill=Component.UNDEFINED, round=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'color', 'fill', 'key', 'loading_state', 'round', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'color', 'fill', 'key', 'loading_state', 'round', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileTag, self).__init__(children=children, **args)
