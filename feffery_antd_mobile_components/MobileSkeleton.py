# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileSkeleton(Component):
    """A MobileSkeleton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- animated (boolean; default False):
    是否开启动画效果  默认：False.

- className (string; optional):
    用于为当前组件设置css类名.

- debug (boolean; default False):
    是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印prop信息  默认：False.

- excludeProps (list of strings; optional):
    设置需要忽略输出监听过程的组件信息列表，仅在listenPropsMode为'exclude'时生效.

- includeProps (list of strings; optional):
    设置需要包含输出监听过程的组件信息列表，仅在listenPropsMode为'include'时生效.

- key (string; optional):
    强制重绘当前组件时使用.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    设置自定义监听组件的模式，可选的有'default'、'exclude'、'include'  默认：'default'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSkeleton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, animated=Component.UNDEFINED, debug=Component.UNDEFINED, listenPropsMode=Component.UNDEFINED, excludeProps=Component.UNDEFINED, includeProps=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'animated', 'className', 'debug', 'excludeProps', 'includeProps', 'key', 'listenPropsMode', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'animated', 'className', 'debug', 'excludeProps', 'includeProps', 'key', 'listenPropsMode', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileSkeleton, self).__init__(children=children, **args)
