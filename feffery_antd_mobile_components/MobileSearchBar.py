# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileSearchBar(Component):
    """A MobileSearchBar component.
搜索框组件MobileSearchBar

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- cancelText (string; default '取消'):
    取消按钮文案  默认：'取消'.

- clearOnCancel (boolean; default True):
    点击取消按钮后是否清空已输入内容  默认：True.

- clearable (boolean; default True):
    是否渲染取消按钮  默认：True.

- icon (a list of or a singular dash component, string or number; optional):
    自定义前缀图标.

- maxLength (number; optional):
    限制允许输入内容的长度上限  默认无限制.

- onlyShowClearWhenFocus (boolean; default False):
    是否仅在当前搜索框聚焦时才显示取消按钮  默认：False.

- placeholder (string; optional):
    提示文本内容.

- showCancelButton (boolean; default False):
    是否在搜索框右侧显示取消按钮  默认：False.

- value (string; optional):
    设置或监听当前搜索框内的已输入文字内容.

- debounceValue (string; optional):
    value的防抖状态值.

- debounceWait (number; default 200):
    针对debounceValue的防抖延时，单位：毫秒  默认：200.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSearchBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, cancelText=Component.UNDEFINED, clearOnCancel=Component.UNDEFINED, clearable=Component.UNDEFINED, icon=Component.UNDEFINED, maxLength=Component.UNDEFINED, onlyShowClearWhenFocus=Component.UNDEFINED, placeholder=Component.UNDEFINED, showCancelButton=Component.UNDEFINED, value=Component.UNDEFINED, debounceValue=Component.UNDEFINED, debounceWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'cancelText', 'clearOnCancel', 'clearable', 'icon', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'showCancelButton', 'value', 'debounceValue', 'debounceWait', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'cancelText', 'clearOnCancel', 'clearable', 'icon', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'showCancelButton', 'value', 'debounceValue', 'debounceWait', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSearchBar, self).__init__(**args)
