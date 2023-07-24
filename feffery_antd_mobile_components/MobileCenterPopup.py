# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileCenterPopup(Component):
    """A MobileCenterPopup component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- id (string; optional):
    用于设置当前组件唯一id.

- bodyClassName (string; optional):
    用于设置内容区域css类.

- bodyStyle (dict; optional):
    用于设置内容区域css样式.

- className (string; optional):
    用于为当前弹出层容器设置css类名.

- closeOnMaskClick (boolean; default False):
    用于设置点击背景蒙板层是否可关闭当前弹出层  默认：False.

- closeOnSwipe (boolean; default False):
    用于设置是否支持上/下滑动关闭弹出层  默认：False.

- destroyOnClose (boolean; default False):
    用于设置当前弹出层内部元素是否在关闭时自动销毁  默认：False.

- forceRender (boolean; default False):
    用于设置初始化时是否强制销毁内部元素  默认：False.

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

- mask (boolean; default True):
    用于设置是否展示蒙板层  默认：True.

- maskClassName (string; optional):
    用于设置蒙板层css类.

- maskStyle (dict; optional):
    用于设置蒙板层css样式.

- showCloseButton (boolean; optional):
    用于设置是否渲染关闭按钮  默认：False.

- style (dict; optional):
    用于为当前弹出层容器设置css样式.

- visible (boolean; default False):
    用于设置或监听当前弹出层是否展开  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCenterPopup'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, visible=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, bodyStyle=Component.UNDEFINED, closeOnMaskClick=Component.UNDEFINED, destroyOnClose=Component.UNDEFINED, forceRender=Component.UNDEFINED, mask=Component.UNDEFINED, maskClassName=Component.UNDEFINED, maskStyle=Component.UNDEFINED, showCloseButton=Component.UNDEFINED, closeOnSwipe=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bodyClassName', 'bodyStyle', 'className', 'closeOnMaskClick', 'closeOnSwipe', 'destroyOnClose', 'forceRender', 'key', 'loading_state', 'mask', 'maskClassName', 'maskStyle', 'showCloseButton', 'style', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bodyClassName', 'bodyStyle', 'className', 'closeOnMaskClick', 'closeOnSwipe', 'destroyOnClose', 'forceRender', 'key', 'loading_state', 'mask', 'maskClassName', 'maskStyle', 'showCloseButton', 'style', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCenterPopup, self).__init__(children=children, **args)
