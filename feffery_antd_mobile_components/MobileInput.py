# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileInput(Component):
    """A MobileInput component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- className (string; optional):
    用于为当前组件设置css类名.

- clearable (boolean; default False):
    是否渲染清除按钮  默认：False.

- debounceValue (string; optional):
    value的防抖状态值.

- debounceWait (number; default 200):
    针对debounceValue的防抖延时，单位：毫秒  默认：200.

- defaultValue (string; optional):
    设置初始化已输入内容.

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

- maxLength (number; optional):
    限制允许输入内容的长度上限  默认无限制.

- onlyShowClearWhenFocus (boolean; default True):
    是否仅在当前输入框聚焦时才显示取消按钮  默认：True.

- placeholder (string; optional):
    提示文本内容.

- readOnly (boolean; default False):
    用于设置是否以只读模式渲染当前组件  默认：False.

- style (dict; optional):
    用于为当前组件设置css样式.

- type (a value equal to: 'text', 'password'; default 'text'):
    用于设置当前输入框的类型  可选的有'text'、'password'  默认：'text'.

- value (string; optional):
    设置或监听当前输入框内的已输入文字内容."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileInput'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, type=Component.UNDEFINED, clearable=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, maxLength=Component.UNDEFINED, onlyShowClearWhenFocus=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, value=Component.UNDEFINED, debounceValue=Component.UNDEFINED, debounceWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'clearable', 'debounceValue', 'debounceWait', 'defaultValue', 'disabled', 'key', 'loading_state', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'readOnly', 'style', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'clearable', 'debounceValue', 'debounceWait', 'defaultValue', 'disabled', 'key', 'loading_state', 'maxLength', 'onlyShowClearWhenFocus', 'placeholder', 'readOnly', 'style', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileInput, self).__init__(**args)
