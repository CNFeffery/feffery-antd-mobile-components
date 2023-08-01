# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileResult(Component):
    """A MobileResult component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- description (a list of or a singular dash component, string or number; optional):
    描述信息.

- icon (a list of or a singular dash component, string or number; optional):
    自定义图标.

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

- status (a value equal to: 'success', 'error', 'info', 'waiting', 'warning'; default 'info'):
    状态类型，可选的有'success'、'error'、'info'、'waiting'、'warning'  默认：'info'.

- style (dict; optional):
    用于为当前组件设置css样式.

- title (a list of or a singular dash component, string or number; optional):
    标题信息."""
    _children_props = ['description', 'icon', 'title']
    _base_nodes = ['description', 'icon', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileResult'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, description=Component.UNDEFINED, icon=Component.UNDEFINED, status=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'description', 'icon', 'key', 'loading_state', 'status', 'style', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'description', 'icon', 'key', 'loading_state', 'status', 'style', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileResult, self).__init__(**args)
