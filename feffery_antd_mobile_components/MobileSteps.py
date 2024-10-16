# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileSteps(Component):
    """A MobileSteps component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- steps (list of dicts; optional):
    用于定义内部各步骤.

    `steps` is a list of dicts with keys:

    - description (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的详情描述内容.

    - icon (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的图标内容.

    - status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
        用于指定当前步骤的状态  可选的有'wait'、'process'、'finish'、'error'
        当不设置时，会自动根据current来指定状态  默认：'wait'.

    - title (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的标题内容.

- current (number; default 0):
    用于设置当前步骤条所在步骤（从0开始计数）  默认：0.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于设置步骤条显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['steps[].description', 'steps[].icon', 'steps[].title']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSteps'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, steps=Component.UNDEFINED, current=Component.UNDEFINED, direction=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'steps', 'current', 'direction', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'steps', 'current', 'direction', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSteps, self).__init__(**args)
