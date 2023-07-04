# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCascaderView(Component):
    """A MobileCascaderView component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultValue (list of strings; optional):
    用于为当前级联选择视图设置默认选中项.

- key (string; optional):
    强制重绘当前组件时使用.

- loading (boolean; default False):
    用于为当前级联选择视图组件设置是否开启加载中状态  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- options (optional):
    用于为当前级联选择视图组件配置级联选项数据  默认：[].

- placeholder (string; default '请选择'):
    用于为当前级联选择视图设置无选中项时的提示文字  默认：'请选择'.

- style (dict; optional):
    用于为当前组件设置css样式.

- value (list of strings; optional):
    用于设置或监听当前已选中项."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCascaderView'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, defaultValue=Component.UNDEFINED, options=Component.UNDEFINED, placeholder=Component.UNDEFINED, value=Component.UNDEFINED, loading=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'defaultValue', 'key', 'loading', 'loading_state', 'options', 'placeholder', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'defaultValue', 'key', 'loading', 'loading_state', 'options', 'placeholder', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCascaderView, self).__init__(**args)
