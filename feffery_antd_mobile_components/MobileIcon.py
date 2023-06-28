# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileIcon(Component):
    """A MobileIcon component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- icon (string; required):
    用于设置当前所使用的图标代号.

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

- nClicks (number; default 0):
    用于记录当前图标累计被点击次数.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileIcon'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, icon=Component.REQUIRED, nClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'icon', 'key', 'loading_state', 'nClicks', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'icon', 'key', 'loading_state', 'nClicks', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['icon']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(MobileIcon, self).__init__(**args)
