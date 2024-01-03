# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobilePopover(Component):
    """A MobilePopover component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置触发目标元素.

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- content (a list of or a singular dash component, string or number; optional):
    设置气泡框内部元素.

- destroyOnHide (boolean; default False):
    隐藏时，是否销毁气泡框内部元素  默认：False.

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

- mode (a value equal to: 'light', 'dark'; default 'light'):
    设置显示模式，可选的有'light'、'dark'  默认：'light'.

- placement (a value equal to: 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; default 'top'):
    设置气泡框位置，可选的有'top'、'top-start'、'top-end'、'right'、'right-start'、'right-end'、'bottom'、'bottom-start'
    、'bottom-end'、'left'、'left-start'、'left-end'  默认：'top'.

- style (dict; optional):
    用于为当前组件设置css样式.

- visible (boolean; optional):
    监听或设置当前气泡框是否处于展开状态."""
    _children_props = ['content']
    _base_nodes = ['content', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePopover'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, content=Component.UNDEFINED, destroyOnHide=Component.UNDEFINED, mode=Component.UNDEFINED, placement=Component.UNDEFINED, visible=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'content', 'destroyOnHide', 'key', 'loading_state', 'mode', 'placement', 'style', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'content', 'destroyOnHide', 'key', 'loading_state', 'mode', 'placement', 'style', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobilePopover, self).__init__(children=children, **args)
