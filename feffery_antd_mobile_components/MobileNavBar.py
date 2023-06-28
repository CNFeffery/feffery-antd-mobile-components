# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileNavBar(Component):
    """A MobileNavBar component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置导航栏标题内容.

- id (string; optional):
    用于设置当前组件唯一id.

- back (a list of or a singular dash component, string or number; default ''):
    用于为当前导航栏设置返回区域文字内容，传入None时会连带返回按钮一起隐藏  默认：''.

- backArrow (boolean | a list of or a singular dash component, string or number; default True):
    用于为当前导航栏设置是否显示返回箭头，也可传入组件型输入充当自定义返回箭头  默认：True.

- className (string; optional):
    用于为当前组件设置css类名.

- key (string; optional):
    强制重绘当前组件时使用.

- left (a list of or a singular dash component, string or number; optional):
    用于设置显示在当前导航栏标题左侧的内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- nBackClicks (number; default 0):
    用于记录当前导航栏返回区域累计被点击次数.

- right (a list of or a singular dash component, string or number; optional):
    用于设置显示在当前导航栏标题右侧的内容.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = ['back', 'backArrow', 'left', 'right']
    _base_nodes = ['back', 'backArrow', 'left', 'right', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileNavBar'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, back=Component.UNDEFINED, backArrow=Component.UNDEFINED, left=Component.UNDEFINED, right=Component.UNDEFINED, nBackClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'back', 'backArrow', 'className', 'key', 'left', 'loading_state', 'nBackClicks', 'right', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'back', 'backArrow', 'className', 'key', 'left', 'loading_state', 'nBackClicks', 'right', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileNavBar, self).__init__(children=children, **args)
