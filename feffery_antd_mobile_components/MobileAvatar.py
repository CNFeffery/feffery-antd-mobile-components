# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileAvatar(Component):
    """A MobileAvatar component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- fallback (a list of or a singular dash component, string or number; optional):
    用于为当前头像组件设置默认占位图.

- fit (a value equal to: 'contain', 'cover', 'fill', 'none', 'scale-down'; default 'cover'):
    用于为当前头像组件设置图片填充模式
    可选的有'contain'、'cover'、'fill'、'none'、'scale-down'  默认：'cover'.

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

- src (string; default ''):
    用于为当前头像组件设置图片地址.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = ['fallback']
    _base_nodes = ['fallback', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileAvatar'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, fallback=Component.UNDEFINED, fit=Component.UNDEFINED, src=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'fallback', 'fit', 'key', 'loading_state', 'src', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'fallback', 'fit', 'key', 'loading_state', 'src', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileAvatar, self).__init__(children=children, **args)
