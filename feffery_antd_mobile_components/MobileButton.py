# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileButton(Component):
    """A MobileButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- block (boolean; default False):
    用于设置当前按钮是否撑满父元素  默认：False.

- className (string; optional):
    用于为当前组件设置css类名.

- color (a value equal to: 'default', 'primary', 'success', 'warning', 'danger'; default 'default'):
    用于设置按钮的颜色状态  可选的有'default'、'primary'、'success'、'warning'、'danger'
    默认：'default'.

- disabled (boolean; default False):
    用于设置是否禁用当前按钮  默认：False.

- fill (a value equal to: 'solid', 'outline', 'none'; default 'solid'):
    用于设置当前按钮的填充模式  可选的有'solid'、'outline'、'none'  默认：'solid'.

- key (string; optional):
    强制重绘当前组件时使用.

- loading (boolean; default False):
    用于设置当前按钮是否处于loading状态  默认：False.

- loadingText (string; optional):
    用于设置loading状态下额外展示的文字内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- nClicks (number; default 0):
    用于记录当前按钮累计被点击次数.

- shape (a value equal to: 'default', 'rounded', 'rectangular'; default 'default'):
    用于设置当前按钮的形状  可选的有'default'、'rounded'、'rectangular'  默认：'default'.

- size (a value equal to: 'mini', 'small', 'middle', 'large'; default 'middle'):
    用于设置当前按钮的尺寸规格  可选的有'mini'、'small'、'middle'、'large'  默认：'middle'.

- style (dict; optional):
    用于为当前组件设置css样式.

- type (a value equal to: 'submit', 'reset', 'button'; default 'button'):
    用于设置当前按钮对应原生html的type属性  可选的有'submit'、'reset'、'button'
    默认：'button'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, block=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, fill=Component.UNDEFINED, loading=Component.UNDEFINED, loadingText=Component.UNDEFINED, shape=Component.UNDEFINED, size=Component.UNDEFINED, type=Component.UNDEFINED, nClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'block', 'className', 'color', 'disabled', 'fill', 'key', 'loading', 'loadingText', 'loading_state', 'nClicks', 'shape', 'size', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'block', 'className', 'color', 'disabled', 'fill', 'key', 'loading', 'loadingText', 'loading_state', 'nClicks', 'shape', 'size', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileButton, self).__init__(children=children, **args)
