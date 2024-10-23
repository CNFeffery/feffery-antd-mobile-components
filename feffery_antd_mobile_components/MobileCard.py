# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCard(Component):
    """A MobileCard component.
卡片组件MobileCard

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- bodyClassName (string; optional):
    用于设置当前卡片body区域css类.

- bodyStyle (dict; optional):
    用于设置当前卡片body区域css样式.

- extra (a list of or a singular dash component, string or number; optional):
    用于为当前卡片设置头部右侧元素.

- headerClassName (string; optional):
    用于设置当前卡片头部区域css类.

- headerStyle (dict; optional):
    用于设置当前卡片头部区域css样式.

- title (a list of or a singular dash component, string or number; optional):
    用于为当前卡片设置头部左侧标题内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['extra', 'title']
    _base_nodes = ['extra', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCard'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, bodyStyle=Component.UNDEFINED, extra=Component.UNDEFINED, headerClassName=Component.UNDEFINED, headerStyle=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'bodyClassName', 'bodyStyle', 'extra', 'headerClassName', 'headerStyle', 'title', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'bodyClassName', 'bodyStyle', 'extra', 'headerClassName', 'headerStyle', 'title', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCard, self).__init__(children=children, **args)
