# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileErrorBlock(Component):
    """A MobileErrorBlock component.
异常组件MobileErrorBlock

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- description (a list of or a singular dash component, string or number; optional):
    额外描述信息.

- fullPage (boolean; default False):
    是否以整页模式进行渲染  默认：False.

- image (string; optional):
    自定义图片链接地址.

- status (a value equal to: 'default', 'disconnected', 'empty', 'busy'; default 'default'):
    预设状态类型，可选的有：'default', 'disconnected', 'empty', 'busy'
    默认：'default'.

- title (a list of or a singular dash component, string or number; optional):
    自定义标题信息.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['description', 'title']
    _base_nodes = ['description', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileErrorBlock'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, description=Component.UNDEFINED, fullPage=Component.UNDEFINED, image=Component.UNDEFINED, status=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'description', 'fullPage', 'image', 'status', 'title', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'description', 'fullPage', 'image', 'status', 'title', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileErrorBlock, self).__init__(children=children, **args)
