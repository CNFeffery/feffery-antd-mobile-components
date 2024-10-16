# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileList(Component):
    """A MobileList component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- items (list of dicts; optional):
    用于定义内部各子项.

    `items` is a list of dicts with keys:

    - key (string; required):
        必填，用于设置当前子项的唯一识别id.

    - arrow (boolean | a list of or a singular dash component, string or number; optional):
        用于设置当前子项右侧是否显示箭头图标  也可传入组件型输入充当自定义图标  默认：与clickable一致.

    - children (a list of or a singular dash component, string or number; optional):
        用于设置当前子项中间区域的主内容.

    - clickable (boolean; optional):
        用于设置当前子项是否展示可点击效果  默认：False.

    - description (a list of or a singular dash component, string or number; optional):
        用于设置当前子项中间下部的描述区域内容.

    - disabled (boolean; optional):
        用于设置是否禁用当前子项  默认：False.

    - extra (a list of or a singular dash component, string or number; optional):
        用于设置当前子项右侧区域内容.

    - prefix (a list of or a singular dash component, string or number; optional):
        用于设置当前子项左侧区域内容.

    - title (a list of or a singular dash component, string or number; optional):
        用于设置当前子项中间上部的标题区域内容.

- title (a list of or a singular dash component, string or number; optional):
    用于设置当前列表标题内容.

- mode (a value equal to: 'default', 'card'; default 'default'):
    用于设置当前列表的渲染方式  可选的有'default'、'card'  默认：'default'.

- clickedItem (dict; optional):
    用于针对可点击的子项，监听点击事件信息.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['items[].arrow', 'items[].children', 'items[].description', 'items[].extra', 'items[].prefix', 'items[].title', 'title']
    _base_nodes = ['title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileList'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, items=Component.UNDEFINED, title=Component.UNDEFINED, mode=Component.UNDEFINED, clickedItem=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'items', 'title', 'mode', 'clickedItem', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'items', 'title', 'mode', 'clickedItem', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileList, self).__init__(**args)
