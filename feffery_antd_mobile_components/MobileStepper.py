# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileStepper(Component):
    """A MobileStepper component.
步进器组件MobileStepper

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

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
    默认值：`False`.

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
    _type = 'MobileStepper'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, allowEmpty=Component.UNDEFINED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, digits=Component.UNDEFINED, disabled=Component.UNDEFINED, inputReadOnly=Component.UNDEFINED, max=Component.UNDEFINED, min=Component.UNDEFINED, step=Component.UNDEFINED, stringMode=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'allowEmpty', 'defaultValue', 'value', 'digits', 'disabled', 'inputReadOnly', 'max', 'min', 'step', 'stringMode', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'allowEmpty', 'defaultValue', 'value', 'digits', 'disabled', 'inputReadOnly', 'max', 'min', 'step', 'stringMode', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileStepper, self).__init__(**args)
