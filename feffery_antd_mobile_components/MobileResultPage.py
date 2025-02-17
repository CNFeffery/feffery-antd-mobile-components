# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileResultPage(Component):
    """A MobileResultPage component.
结果页面组件MobileResultPage

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素，推荐配合`MobileResultPageCard`.

- title (a list of or a singular dash component, string or number; optional):
    组件型，结果标题信息.

- description (a list of or a singular dash component, string or number; optional):
    组件型，结果描述信息.

- icon (a list of or a singular dash component, string or number; optional):
    组件型，结果标题内容.

- details (list of dicts; optional):
    配置结果页详情信息项.

    `details` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        组件型，当前信息项标题.

    - value (a list of or a singular dash component, string or number; optional):
        组件型，当前信息项内容.

    - bold (boolean; optional):
        当前信息项是否加粗  默认值：`False`.

- status (a value equal to: 'success', 'error', 'info', 'waiting', 'warning'; default 'info'):
    结果页状态类型，可选项有`'success'`、`'error'`、`'info'`、`'waiting'`、`'warning'`
    默认值：`'info'`.

- primaryButtonText (a list of or a singular dash component, string or number; optional):
    主要操作按钮内嵌内容，传入空值时不显示主要按钮.

- secondaryButtonText (a list of or a singular dash component, string or number; optional):
    辅助操作按钮内嵌内容，传入空值时不显示辅助操作按钮.

- nClicksPrimary (number; default 0):
    监听主要操作按钮累计点击次数  默认值：`0`.

- nClicksSecondary (number; default 0):
    监听辅助操作按钮累计点击次数  默认值：`0`."""
    _children_props = ['title', 'description', 'icon', 'details[].label', 'details[].value', 'primaryButtonText', 'secondaryButtonText']
    _base_nodes = ['title', 'description', 'icon', 'primaryButtonText', 'secondaryButtonText', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileResultPage'
    Details = TypedDict(
        "Details",
            {
            "label": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "value": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "bold": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        title: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        description: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        icon: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        details: typing.Optional[typing.Sequence["Details"]] = None,
        status: typing.Optional[Literal["success", "error", "info", "waiting", "warning"]] = None,
        primaryButtonText: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        secondaryButtonText: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        nClicksPrimary: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        nClicksSecondary: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'title', 'description', 'icon', 'details', 'status', 'primaryButtonText', 'secondaryButtonText', 'nClicksPrimary', 'nClicksSecondary']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'title', 'description', 'icon', 'details', 'status', 'primaryButtonText', 'secondaryButtonText', 'nClicksPrimary', 'nClicksSecondary']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileResultPage, self).__init__(children=children, **args)
