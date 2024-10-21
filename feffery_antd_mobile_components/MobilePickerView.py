# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobilePickerView(Component):
    """A MobilePickerView component.
选择器视图组件MobilePickerView

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- columns (list of dicts; optional):
    配置各列选项.

    `columns` is a list of list of dicts with keys:

    - label (string; optional):
        当前选项标题.

    - value (string; optional):
        当前选项值.s

- defaultValue (list of strings; optional):
    设置默认选中值  默认值：`[]`.

- value (list of strings; optional):
    监听或设置当前选中值.

- mouseWheel (boolean; default False):
    是否启用鼠标滚轮辅助选择  默认值：`False`.

- loading (boolean; default False):
    设置是否渲染为“加载中”状态  默认值：`False`.

- loadingContent (a list of or a singular dash component, string or number; optional):
    组件型，“加载中”状态下展示的内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['loadingContent']
    _base_nodes = ['loadingContent', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePickerView'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, columns=Component.UNDEFINED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, mouseWheel=Component.UNDEFINED, loading=Component.UNDEFINED, loadingContent=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'columns', 'defaultValue', 'value', 'mouseWheel', 'loading', 'loadingContent', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'columns', 'defaultValue', 'value', 'mouseWheel', 'loading', 'loadingContent', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobilePickerView, self).__init__(**args)
