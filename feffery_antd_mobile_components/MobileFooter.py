# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileFooter(Component):
    """A MobileFooter component.
页脚组件MobileFooter

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- label (string | a list of or a singular dash component, string or number; optional):
    用于为当前页脚设置分割线内部元素.

- links (list of dicts; optional):
    用于为当前页脚设置链接部分内容.

    `links` is a list of dicts with keys:

    - text (string; optional):
        用于为当前链接项设置链接文字.

    - href (string; optional):
        用于为当前链接项设置链接地址.

- content (string | a list of or a singular dash component, string or number; optional):
    用于为当前页脚设置内容区域元素.

- chips (list of dicts; optional):
    用于为当前页脚设置底部标签部分内容.

    `chips` is a list of dicts with keys:

    - text (string | a list of or a singular dash component, string or number; optional):
        用于设置当前标签项的内容.

    - type (a value equal to: 'plain', 'link'; optional):
        用于设置当前标签项的类型  可选的有'plain'（纯展示）、'link'（可点击）  默认：'plain'.

    - key (string; optional):
        用于为当前标签设置唯一识别id，用于在可点击类型下监听标签点击事件.

- clickedChip (dict; optional):
    用于针对可点击的标签项，监听点击事件信息.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['label', 'content', 'chips[].text']
    _base_nodes = ['label', 'content', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileFooter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, label=Component.UNDEFINED, links=Component.UNDEFINED, content=Component.UNDEFINED, chips=Component.UNDEFINED, clickedChip=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'label', 'links', 'content', 'chips', 'clickedChip', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'label', 'links', 'content', 'chips', 'clickedChip', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileFooter, self).__init__(**args)
