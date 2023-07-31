# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCheckboxGroup(Component):
    """A MobileCheckboxGroup component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- block (boolean; default True):
    每个选项是否独占一行  默认：True.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultValue (list of strings; optional):
    设置初始化时选中值对应数组  默认：[].

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

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

- options (list of dicts; optional):
    用于为当前复选框组定义选项.

    `options` is a list of dicts with keys:

    - className (string; optional):
        当前项css类名.

    - disabled (boolean; optional):
        是否禁用当前项  默认：False.

    - label (a list of or a singular dash component, string or number; optional):
        当前项标签内容.

    - style (dict; optional):
        当前项css样式.

    - value (string; optional):
        当前项对应值.

- style (dict; optional):
    用于为当前组件设置css样式.

- value (list of strings; optional):
    设置或监听已选中值对应数组."""
    _children_props = ['options[].label']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckboxGroup'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, options=Component.UNDEFINED, block=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, value=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'block', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'block', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCheckboxGroup, self).__init__(**args)
