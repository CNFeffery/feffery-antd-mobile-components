# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileCheckList(Component):
    """A MobileCheckList component.
可勾选列表组件MobileCheckList

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- style (dict; optional):
    用于为当前组件设置css样式.

- className (string; optional):
    用于为当前组件设置css类名.

- options (list of dicts; optional):
    用于为当前可勾选列表定义选项.

    `options` is a list of dicts with keys:

    - children (a list of or a singular dash component, string or number; optional):
        用于设置当前选项主要区域元素.

    - value (string; optional):
        用于设置当前选项的值.

    - title (a list of or a singular dash component, string or number; optional):
        用于设置当前选项中间上部的标题区域元素.

    - description (a list of or a singular dash component, string or number; optional):
        用于设置当前选项中间下部的描述区域元素.

    - prefix (a list of or a singular dash component, string or number; optional):
        用于设置当前选项左侧区域元素.

    - disabled (boolean; optional):
        用于设置是否禁用当前选项  默认：False.

    - readOnly (boolean; optional):
        用于设置是否以只读模式渲染当前选项  默认：False.

- defaultValue (list of strings; optional):
    用于设置当前可勾选列表组件的默认选中项.

- disabled (boolean; default False):
    用于设置是否禁用当前组件  默认：False.

- multiple (boolean; default False):
    用于设置是否允许多选  默认：False.

- readOnly (boolean; default False):
    用于设置是否以只读模式渲染当前组件  默认：False.

- value (list of strings; optional):
    用于设置或监听当前可勾选列表组件的选中项."""
    _children_props = ['options[].children', 'options[].title', 'options[].description', 'options[].prefix']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckList'
    Options = TypedDict(
        "Options",
            {
            "children": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "value": NotRequired[str],
            "title": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "description": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "prefix": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "disabled": NotRequired[bool],
            "readOnly": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        options: typing.Optional[typing.Sequence["Options"]] = None,
        defaultValue: typing.Optional[typing.Sequence[str]] = None,
        disabled: typing.Optional[bool] = None,
        multiple: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        value: typing.Optional[typing.Sequence[str]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'options', 'defaultValue', 'disabled', 'multiple', 'readOnly', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'options', 'defaultValue', 'disabled', 'multiple', 'readOnly', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCheckList, self).__init__(**args)
