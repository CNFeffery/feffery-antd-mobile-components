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


class MobileActionSheet(Component):
    """A MobileActionSheet component.
动作面板组件MobileActionSheet

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- actions (list of dicts; optional):
    配置面板选项.

    `actions` is a list of dicts with keys:

    - key (string; required):
        必填，当前选项唯一标识.

    - text (string; required):
        必填，当前选项标题.

    - description (string; optional):
        当前选项描述信息.

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`.

    - danger (boolean; optional):
        当前选项是否渲染为危险状态  默认值：`False`.

    - bold (boolean; optional):
        当前选项标题是否加粗  默认值：`False`.

- cancelText (a list of or a singular dash component, string or number; optional):
    组件型，取消按钮内容，不设置时不显示取消按钮.

- closeOnAction (boolean; default False):
    点击选项后是否自动关闭面板  默认值：`False`.

- closeOnMaskClick (boolean; default True):
    是否可通过点击背景蒙版层关闭面板  默认值：`True`.

- destroyOnClose (boolean; default False):
    面板不可见时是否销毁内部元素  默认值：`False`.

- forceRender (boolean; default False):
    是否强制渲染内部元素  默认值：`False`.

- extra (a list of or a singular dash component, string or number; optional):
    组件型，顶部额外内容.

- popupClassName (string; optional):
    弹出层css类名.

- safeArea (boolean; default True):
    是否开启安全区适配  默认值：`True`.

- visible (boolean; default False):
    监听或设置当前面板显示状态  默认值：`False`.

- actionEvent (dict; optional):
    监听指令点击触发事件.

    `actionEvent` is a dict with keys:

    - key (string; optional):
        对应指令项`key`值.

    - timestamp (number; optional):
        事件对应时间戳.

- styles (dict; optional):
    语义化结构css样式.

    `styles` is a dict with keys:

    - body (dict; optional):
        内容区css样式.

    - mask (dict; optional):
        背景蒙版层css样式."""
    _children_props = ['cancelText', 'extra']
    _base_nodes = ['cancelText', 'extra', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileActionSheet'
    Actions = TypedDict(
        "Actions",
            {
            "key": str,
            "text": str,
            "description": NotRequired[str],
            "disabled": NotRequired[bool],
            "danger": NotRequired[bool],
            "bold": NotRequired[bool]
        }
    )

    ActionEvent = TypedDict(
        "ActionEvent",
            {
            "key": NotRequired[str],
            "timestamp": NotRequired[NumberType]
        }
    )

    Styles = TypedDict(
        "Styles",
            {
            "body": NotRequired[dict],
            "mask": NotRequired[dict]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        actions: typing.Optional[typing.Sequence["Actions"]] = None,
        cancelText: typing.Optional[ComponentType] = None,
        closeOnAction: typing.Optional[bool] = None,
        closeOnMaskClick: typing.Optional[bool] = None,
        destroyOnClose: typing.Optional[bool] = None,
        forceRender: typing.Optional[bool] = None,
        extra: typing.Optional[ComponentType] = None,
        popupClassName: typing.Optional[str] = None,
        safeArea: typing.Optional[bool] = None,
        visible: typing.Optional[bool] = None,
        actionEvent: typing.Optional["ActionEvent"] = None,
        styles: typing.Optional["Styles"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'actions', 'cancelText', 'closeOnAction', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'extra', 'popupClassName', 'safeArea', 'visible', 'actionEvent', 'styles']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'actions', 'cancelText', 'closeOnAction', 'closeOnMaskClick', 'destroyOnClose', 'forceRender', 'extra', 'popupClassName', 'safeArea', 'visible', 'actionEvent', 'styles']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileActionSheet, self).__init__(**args)

setattr(MobileActionSheet, "__init__", _explicitize_args(MobileActionSheet.__init__))
