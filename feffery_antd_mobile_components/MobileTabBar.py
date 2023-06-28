# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileTabBar(Component):
    """A MobileTabBar component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- activeKey (string; optional):
    用于设置或监听当前被激活的选项对应key值.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultActiveKey (string; optional):
    用于设置初始化时，处于被激活状态的选项对应key值  默认激活items中按顺序第一位的选项.

- items (list of dicts; optional):
    用于定义内部各选项相关信息.

    `items` is a list of dicts with keys:

    - badge (a list of or a singular dash component, string or number; optional):
        用于为当前选项设置额外的徽标信息  特别地，当传入'dot'时会渲染小红点徽标.

    - icon (a list of or a singular dash component, string or number; optional):
        用于设置当前选项对应的额外图标.

    - key (string; required):
        必填，用于设置当前选项对应的唯一标识值.

    - title (a list of or a singular dash component, string or number; required):
        必填，用于设置当前选项对应的标题内容.

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

- safeArea (boolean; default False):
    用于设置是否开启安全区适配功能  默认：False.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = ['items[].title', 'items[].icon', 'items[].badge']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileTabBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, items=Component.UNDEFINED, activeKey=Component.UNDEFINED, defaultActiveKey=Component.UNDEFINED, safeArea=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'activeKey', 'className', 'defaultActiveKey', 'items', 'key', 'loading_state', 'safeArea', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activeKey', 'className', 'defaultActiveKey', 'items', 'key', 'loading_state', 'safeArea', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileTabBar, self).__init__(**args)