# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileFormItem(Component):
    """A MobileFormItem component.
表单项组件MobileFormItem

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
    用于传入内部各MobileFormItem表单项组件.

- childElementPosition (a value equal to: 'normal', 'right'; default 'normal'):
    表单项控件的位置，可选的有'normal'、'right'  默认：'normal'.

- disabled (boolean; optional):
    是否禁用当前组件  默认：False.

- help (a list of or a singular dash component, string or number; optional):
    额外提示信息.

- hidden (boolean; default False):
    是否隐藏当前表单项  默认：False.

- label (a list of or a singular dash component, string or number; optional):
    标签内容.

- layout (a value equal to: 'vertical', 'horizontal'; optional):
    自定义布局模式，可选的有'vertical'、'horizontal'  默认以父级表单组件的布局模式为准.

- required (boolean; default False):
    是否显示必选标记  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['help', 'label']
    _base_nodes = ['help', 'label', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileFormItem'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, childElementPosition=Component.UNDEFINED, disabled=Component.UNDEFINED, help=Component.UNDEFINED, hidden=Component.UNDEFINED, label=Component.UNDEFINED, layout=Component.UNDEFINED, required=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'childElementPosition', 'disabled', 'help', 'hidden', 'label', 'layout', 'required', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'childElementPosition', 'disabled', 'help', 'hidden', 'label', 'layout', 'required', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileFormItem, self).__init__(children=children, **args)
