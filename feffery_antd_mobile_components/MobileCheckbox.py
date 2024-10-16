# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCheckbox(Component):
    """A MobileCheckbox component.


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
    用于设置当前复选框标签内容.

- block (boolean; default False):
    是否撑满父级元素  默认：False.

- checked (boolean; default False):
    设置或监听当前复选框是否选中  默认：False.

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- icon (dict; optional):
    自定义各状态下的图标元素.

    `icon` is a dict with keys:

    - checked (a list of or a singular dash component, string or number; optional):
        自定义选中状态下图标元素.

    - unchecked (a list of or a singular dash component, string or number; optional):
        自定义非选中状态下图标元素.

    - indeterminate (a list of or a singular dash component, string or number; optional):
        自定义半选中状态下图标元素.

- indeterminate (boolean; default False):
    是否以半选中状态进行渲染，仅用作样式控制.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['icon.checked', 'icon.unchecked', 'icon.indeterminate']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckbox'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, block=Component.UNDEFINED, checked=Component.UNDEFINED, disabled=Component.UNDEFINED, icon=Component.UNDEFINED, indeterminate=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'block', 'checked', 'disabled', 'icon', 'indeterminate', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'block', 'checked', 'disabled', 'icon', 'indeterminate', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCheckbox, self).__init__(children=children, **args)
