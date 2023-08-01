# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileForm(Component):
    """A MobileForm component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于传入内部各MobileFormItem表单项组件.

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- footer (a list of or a singular dash component, string or number; optional):
    自定义表单底部元素.

- key (string; optional):
    强制重绘当前组件时使用.

- layout (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    布局模式，可选的有'vertical'、'horizontal'  默认：'vertical'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- mode (a value equal to: 'default', 'card'; default 'default'):
    渲染模式，可选的有'default'、'card'  默认：'default'.

- requiredMarkStyle (a value equal to: 'asterisk', 'text-required', 'text-optional', 'none'; default 'asterisk'):
    针对内部表单项的必填选填标记样式类型进行设置
    可选的有'asterisk'、'text-required'、'text-optional'、'none'
    默认：'asterisk'.

- style (dict; optional):
    用于为当前组件设置css样式."""
    _children_props = ['footer']
    _base_nodes = ['footer', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileForm'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, disabled=Component.UNDEFINED, footer=Component.UNDEFINED, layout=Component.UNDEFINED, mode=Component.UNDEFINED, requiredMarkStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'footer', 'key', 'layout', 'loading_state', 'mode', 'requiredMarkStyle', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'footer', 'key', 'layout', 'loading_state', 'mode', 'requiredMarkStyle', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileForm, self).__init__(children=children, **args)
