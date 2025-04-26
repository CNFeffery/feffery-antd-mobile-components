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


class MobileStepper(Component):
    """A MobileStepper component.
步进器组件MobileStepper

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- allowEmpty (boolean; default False):
    是否允许输入内容为空  默认值：`False`.

- defaultValue (number | string; default 0):
    设置默认输入值  默认值：`0`.

- value (number | string; optional):
    监听或设置输入值.

- digits (number; optional):
    格式化对应小数点后固定位数.

- disabled (boolean; default False):
    是否禁用当前步进器  默认值：`False`.

- inputReadOnly (boolean; default False):
    输入框是否只读  默认值：`False`.

- max (number | string; optional):
    限定最大值.

- min (number | string; optional):
    限定最小值.

- step (number | string; default 1):
    步进对应数值步长  默认值：`1`.

- stringMode (boolean; default False):
    是否开启高精度字符值模式，开启后`defaultValue`、`value`、`min`、`max`等参数为字符型
    默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileStepper'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        allowEmpty: typing.Optional[bool] = None,
        defaultValue: typing.Optional[typing.Union[NumberType, str]] = None,
        value: typing.Optional[typing.Union[NumberType, str]] = None,
        digits: typing.Optional[NumberType] = None,
        disabled: typing.Optional[bool] = None,
        inputReadOnly: typing.Optional[bool] = None,
        max: typing.Optional[typing.Union[NumberType, str]] = None,
        min: typing.Optional[typing.Union[NumberType, str]] = None,
        step: typing.Optional[typing.Union[NumberType, str]] = None,
        stringMode: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'allowEmpty', 'defaultValue', 'value', 'digits', 'disabled', 'inputReadOnly', 'max', 'min', 'step', 'stringMode']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'allowEmpty', 'defaultValue', 'value', 'digits', 'disabled', 'inputReadOnly', 'max', 'min', 'step', 'stringMode']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileStepper, self).__init__(**args)

setattr(MobileStepper, "__init__", _explicitize_args(MobileStepper.__init__))
