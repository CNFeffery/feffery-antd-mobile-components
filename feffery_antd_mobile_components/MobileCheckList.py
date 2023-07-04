# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCheckList(Component):
    """A MobileCheckList component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- defaultValue (list of strings; optional):
    用于设置当前可勾选列表组件的默认选中项.

- disabled (boolean; default False):
    用于设置是否禁用当前组件  默认：False.

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

- multiple (boolean; default False):
    用于设置是否允许多选  默认：False.

- options (list of dicts; optional):
    用于为当前可勾选列表定义选项.

    `options` is a list of dicts with keys:

    - children (a list of or a singular dash component, string or number; optional):
        用于设置当前选项主要区域元素.

    - description (a list of or a singular dash component, string or number; optional):
        用于设置当前选项中间下部的描述区域元素.

    - disabled (boolean; optional):
        用于设置是否禁用当前选项  默认：False.

    - prefix (a list of or a singular dash component, string or number; optional):
        用于设置当前选项左侧区域元素.

    - readOnly (boolean; optional):
        用于设置是否以只读模式渲染当前选项  默认：False.

    - title (a list of or a singular dash component, string or number; optional):
        用于设置当前选项中间上部的标题区域元素.

    - value (string; optional):
        用于设置当前选项的值.

- readOnly (boolean; default False):
    用于设置是否以只读模式渲染当前组件  默认：False.

- style (dict; optional):
    用于为当前组件设置css样式.

- value (list of strings; optional):
    用于设置或监听当前可勾选列表组件的选中项."""
    _children_props = ['options[].children', 'options[].title', 'options[].description', 'options[].prefix']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckList'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, options=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, multiple=Component.UNDEFINED, readOnly=Component.UNDEFINED, value=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'multiple', 'options', 'readOnly', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'multiple', 'options', 'readOnly', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCheckList, self).__init__(**args)
