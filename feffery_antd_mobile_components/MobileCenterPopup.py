# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class MobileCenterPopup(Component):
    """A MobileCenterPopup component.
居中弹出层组件MobileCenterPopup

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

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

- showCloseButton (boolean; optional):
    用于设置是否渲染关闭按钮  默认：False.

- closeOnSwipe (boolean; default False):
    用于设置是否支持上/下滑动关闭弹出层  默认：False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCenterPopup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        visible: typing.Optional[bool] = None,
        bodyClassName: typing.Optional[str] = None,
        bodyStyle: typing.Optional[dict] = None,
        closeOnMaskClick: typing.Optional[bool] = None,
        destroyOnClose: typing.Optional[bool] = None,
        forceRender: typing.Optional[bool] = None,
        mask: typing.Optional[bool] = None,
        maskClassName: typing.Optional[str] = None,
        maskStyle: typing.Optional[dict] = None,
        showCloseButton: typing.Optional[bool] = None,
        closeOnSwipe: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'visible', 'bodyClassName', 'bodyStyle', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'mask', 'maskClassName', 'maskStyle', 'showCloseButton', 'closeOnSwipe']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'visible', 'bodyClassName', 'bodyStyle', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'mask', 'maskClassName', 'maskStyle', 'showCloseButton', 'closeOnSwipe']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileCenterPopup, self).__init__(children=children, **args)

setattr(MobileCenterPopup, "__init__", _explicitize_args(MobileCenterPopup.__init__))
