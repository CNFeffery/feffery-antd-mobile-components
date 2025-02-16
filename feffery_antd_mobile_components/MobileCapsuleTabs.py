# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileCapsuleTabs(Component):
    """A MobileCapsuleTabs component.
胶囊选项卡组件MobileCapsuleTabs

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- items (list of dicts; optional):
    用于定义内部各选项相关信息.

    `items` is a list of dicts with keys:

    - key (string; required):
        必填，用于设置当前选项对应的唯一标识值.

    - title (a list of or a singular dash component, string or number; required):
        必填，用于设置当前选项对应的标题内容.

    - children (a list of or a singular dash component, string or number; optional):
        可选，用于设置当前选项对应的内容.

    - disabled (boolean; optional):
        用于设置是否禁用当前选项  默认：False.

    - forceRender (boolean; optional):
        用于设置初始化时，若当前选项不可见，是否对其对应的children内容进行渲染  默认：False.

    - destroyOnClose (boolean; optional):
        用于设置当前选项被隐藏后，是否对其children内容进行销毁  默认：False.

- activeKey (string; optional):
    用于设置或监听当前被激活的选项对应key值.

- defaultActiveKey (string; optional):
    用于设置初始化时，处于被激活状态的选项对应key值  默认激活items中按顺序第一位的选项."""
    _children_props = ['items[].title', 'items[].children']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCapsuleTabs'
    Items = TypedDict(
        "Items",
            {
            "key": str,
            "title": typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]],
            "children": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "disabled": NotRequired[bool],
            "forceRender": NotRequired[bool],
            "destroyOnClose": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        items: typing.Optional[typing.Sequence["Items"]] = None,
        activeKey: typing.Optional[str] = None,
        defaultActiveKey: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'items', 'activeKey', 'defaultActiveKey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'items', 'activeKey', 'defaultActiveKey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCapsuleTabs, self).__init__(**args)
