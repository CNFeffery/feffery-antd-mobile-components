# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileToast(Component):
    """A MobileToast component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- content (a list of or a singular dash component, string or number; optional):
    轻提示内容.

- duration (number; default 2000):
    持续显示时长，单位：毫秒  默认：2000.

- icon (a value equal to: 'success', 'fail', 'loading'; optional):
    额外图标类型，可选的有'success'、'fail'、'loading'.

- maskClassName (string; optional):
    遮罩层css类名.

- maskClickable (boolean; default True):
    背景是否可点击  默认：True.

- maskStyle (dict; optional):
    遮罩层css样式.

- position (a value equal to: 'top', 'bottom', 'center'; default 'center'):
    垂直方向显示位置，可选的有'top'、'bottom'、'center'  默认：'center'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['content']
    _base_nodes = ['content', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileToast'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, content=Component.UNDEFINED, duration=Component.UNDEFINED, icon=Component.UNDEFINED, maskClassName=Component.UNDEFINED, maskClickable=Component.UNDEFINED, maskStyle=Component.UNDEFINED, position=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'content', 'duration', 'icon', 'maskClassName', 'maskClickable', 'maskStyle', 'position', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'content', 'duration', 'icon', 'maskClassName', 'maskClickable', 'maskStyle', 'position', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileToast, self).__init__(**args)
