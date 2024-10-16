# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCascader(Component):
    """A MobileCascader component.


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
    用于为当前级联选择设置取消按钮文案信息  默认：'取消'.

- confirmText (string; default '确认'):
    用于为当前级联选择设置确认按钮文案信息  默认：'确认'.

- defaultValue (list of strings; optional):
    用于为当前级联选择设置默认选中项.

- destroyOnClose (boolean; default True):
    当前级联选择组件不可见时是否进行销毁  默认：True.

- forceRender (boolean; default False):
    用于设置初始化时是否强制渲染当前级联选择组件  默认：False.

- options (optional):
    用于为当前级联选择组件配置级联选项数据  默认：[].

- placeholder (string; default '请选择'):
    用于为当前级联选择设置无选中项时的提示文字  默认：'请选择'.

- title (string | a list of or a singular dash component, string or number; optional):
    为当前级联选择设置标题内容.

- value (list of strings; optional):
    用于设置或监听当前已选中项.

- visible (boolean; default False):
    用于设置是否显示当前级联选择  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['title']
    _base_nodes = ['title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCascader'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, cancelText=Component.UNDEFINED, confirmText=Component.UNDEFINED, defaultValue=Component.UNDEFINED, destroyOnClose=Component.UNDEFINED, forceRender=Component.UNDEFINED, options=Component.UNDEFINED, placeholder=Component.UNDEFINED, title=Component.UNDEFINED, value=Component.UNDEFINED, visible=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'cancelText', 'confirmText', 'defaultValue', 'destroyOnClose', 'forceRender', 'options', 'placeholder', 'title', 'value', 'visible', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'cancelText', 'confirmText', 'defaultValue', 'destroyOnClose', 'forceRender', 'options', 'placeholder', 'title', 'value', 'visible', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCascader, self).__init__(**args)
