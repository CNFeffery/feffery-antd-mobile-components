# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobilePopup(Component):
    """A MobilePopup component.


Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前弹出层容器设置css样式.

- className (string; optional):
    用于为当前弹出层容器设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- visible (boolean; default False):
    用于设置或监听当前弹出层是否展开  默认：False.

- bodyClassName (string; optional):
    用于设置内容区域css类.

- bodyStyle (dict; optional):
    用于设置内容区域css样式.

- closeOnMaskClick (boolean; default False):
    用于设置点击背景蒙板层是否可关闭当前弹出层  默认：False.

- destroyOnClose (boolean; default False):
    用于设置当前弹出层内部元素是否在关闭时自动销毁  默认：False.

- forceRender (boolean; default False):
    用于设置初始化时是否强制销毁内部元素  默认：False.

- mask (boolean; default True):
    用于设置是否展示蒙板层  默认：True.

- maskClassName (string; optional):
    用于设置蒙板层css类.

- maskStyle (dict; optional):
    用于设置蒙板层css样式.

- position (a value equal to: 'bottom', 'top', 'left', 'right'; default 'bottom'):
    用于设置当前弹出层弹出位置  可选的有'bottom'、'top'、'left'、'right'  默认：'bottom'.

- showCloseButton (boolean; optional):
    用于设置是否渲染关闭按钮  默认：False.

- closeOnSwipe (boolean; default False):
    用于设置是否支持上/下滑动关闭弹出层  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePopup'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, visible=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, bodyStyle=Component.UNDEFINED, closeOnMaskClick=Component.UNDEFINED, destroyOnClose=Component.UNDEFINED, forceRender=Component.UNDEFINED, mask=Component.UNDEFINED, maskClassName=Component.UNDEFINED, maskStyle=Component.UNDEFINED, position=Component.UNDEFINED, showCloseButton=Component.UNDEFINED, closeOnSwipe=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'visible', 'bodyClassName', 'bodyStyle', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'mask', 'maskClassName', 'maskStyle', 'position', 'showCloseButton', 'closeOnSwipe', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'visible', 'bodyClassName', 'bodyStyle', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'mask', 'maskClassName', 'maskStyle', 'position', 'showCloseButton', 'closeOnSwipe', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobilePopup, self).__init__(children=children, **args)
