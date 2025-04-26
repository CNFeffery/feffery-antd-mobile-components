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


class MobileDialog(Component):
    """A MobileDialog component.
对话框组件MobileDialog

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- actions (list of dicts; optional):
    配置操作按钮，可传入二级数组实现同一行并排显示多个按钮.

    `actions` is a list of dicts with keys:

    - key (string; required):
        必填，当前选项唯一标识.

    - text (string; required):
        必填，当前选项标题.

    - style (dict; optional):
        当前选项css样式.

    - className (string; optional):
        当前选项css类名.

    - bold (boolean; optional):
        当前选项文字是否加粗  默认值：`False`.

    - danger (boolean; optional):
        当前选项是否渲染为危险状态  默认值：`False`.

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`. | list of dicts with keys:

    - key (string; required):
        必填，当前选项唯一标识.

    - text (string; required):
        必填，当前选项标题.

    - style (dict; optional):
        当前选项css样式.

    - className (string; optional):
        当前选项css类名.

    - bold (boolean; optional):
        当前选项文字是否加粗  默认值：`False`.

    - danger (boolean; optional):
        当前选项是否渲染为危险状态  默认值：`False`.

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`.

- bodyClassName (string; optional):
    内容区css类名.

- bodyStyle (dict; optional):
    内容区css样式.

- closeOnAction (boolean; default False):
    点击操作按钮后是否自动关闭对话框  默认值：`False`.

- closeOnMaskClick (boolean; default False):
    是否可通过点击遮罩关闭对话框  默认值：`False`.

- content (a list of or a singular dash component, string or number; optional):
    组件型，对话框内容.

- destroyOnClose (boolean; default False):
    对话框不可见时是否销毁内部元素  默认值：`False`.

- disableBodyScroll (boolean; default True):
    是否禁用内容区滚动  默认值：`True`.

- forceRender (boolean; default False):
    是否强制渲染内部元素  默认值：`False`.

- header (a list of or a singular dash component, string or number; optional):
    组件型，对话框顶部区域内容.

- image (string; optional):
    内部图片地址.

- maskClassName (string; optional):
    遮罩层css类名.

- maskStyle (dict; optional):
    遮罩层css样式.

- title (a list of or a singular dash component, string or number; optional):
    组件型，对话框标题内容.

- visible (boolean; default False):
    监听或设置当前对话框是否显示  默认值：`False`.

- actionEvent (dict; optional):
    监听指令点击触发事件.

    `actionEvent` is a dict with keys:

    - key (string; optional):
        对应指令项`key`值.

    - timestamp (number; optional):
        事件对应时间戳."""
    _children_props = ['content', 'header', 'title']
    _base_nodes = ['content', 'header', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileDialog'
    Actions = TypedDict(
        "Actions",
            {
            "key": str,
            "text": str,
            "style": NotRequired[dict],
            "className": NotRequired[str],
            "bold": NotRequired[bool],
            "danger": NotRequired[bool],
            "disabled": NotRequired[bool]
        }
    )

    ActionEvent = TypedDict(
        "ActionEvent",
            {
            "key": NotRequired[str],
            "timestamp": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        actions: typing.Optional[typing.Sequence[typing.Union["Actions", typing.Sequence["Actions"]]]] = None,
        bodyClassName: typing.Optional[str] = None,
        bodyStyle: typing.Optional[dict] = None,
        closeOnAction: typing.Optional[bool] = None,
        closeOnMaskClick: typing.Optional[bool] = None,
        content: typing.Optional[ComponentType] = None,
        destroyOnClose: typing.Optional[bool] = None,
        disableBodyScroll: typing.Optional[bool] = None,
        forceRender: typing.Optional[bool] = None,
        header: typing.Optional[ComponentType] = None,
        image: typing.Optional[str] = None,
        maskClassName: typing.Optional[str] = None,
        maskStyle: typing.Optional[dict] = None,
        title: typing.Optional[ComponentType] = None,
        visible: typing.Optional[bool] = None,
        actionEvent: typing.Optional["ActionEvent"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'actions', 'bodyClassName', 'bodyStyle', 'closeOnAction', 'closeOnMaskClick', 'content', 'destroyOnClose', 'disableBodyScroll', 'forceRender', 'header', 'image', 'maskClassName', 'maskStyle', 'title', 'visible', 'actionEvent']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'actions', 'bodyClassName', 'bodyStyle', 'closeOnAction', 'closeOnMaskClick', 'content', 'destroyOnClose', 'disableBodyScroll', 'forceRender', 'header', 'image', 'maskClassName', 'maskStyle', 'title', 'visible', 'actionEvent']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileDialog, self).__init__(**args)

setattr(MobileDialog, "__init__", _explicitize_args(MobileDialog.__init__))
