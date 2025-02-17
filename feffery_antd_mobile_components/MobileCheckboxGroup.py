# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MobileCheckboxGroup(Component):
    """A MobileCheckboxGroup component.
复选框组合组件MobileCheckboxGroup

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
    用于为当前复选框组定义选项.

    `options` is a list of dicts with keys:

    - disabled (boolean; optional):
        是否禁用当前项  默认：False.

    - label (a list of or a singular dash component, string or number; optional):
        当前项标签内容.

    - value (string; optional):
        当前项对应值.

    - style (dict; optional):
        当前项css样式.

    - className (string; optional):
        当前项css类名.

- block (boolean; default True):
    每个选项是否独占一行  默认：True.

- defaultValue (list of strings; optional):
    设置初始化时选中值对应数组  默认：[].

- disabled (boolean; default False):
    是否禁用当前组件  默认：False.

- value (list of strings; optional):
    设置或监听已选中值对应数组."""
    _children_props = ['options[].label']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileCheckboxGroup'
    Options = TypedDict(
        "Options",
            {
            "disabled": NotRequired[bool],
            "label": NotRequired[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]],
            "value": NotRequired[str],
            "style": NotRequired[dict],
            "className": NotRequired[str]
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
        block: typing.Optional[bool] = None,
        defaultValue: typing.Optional[typing.Sequence[str]] = None,
        disabled: typing.Optional[bool] = None,
        value: typing.Optional[typing.Sequence[str]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'options', 'block', 'defaultValue', 'disabled', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'options', 'block', 'defaultValue', 'disabled', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileCheckboxGroup, self).__init__(**args)
