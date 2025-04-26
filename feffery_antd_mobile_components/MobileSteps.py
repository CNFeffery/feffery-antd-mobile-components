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


class MobileSteps(Component):
    """A MobileSteps component.
步骤条组件MobileSteps

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- steps (list of dicts; optional):
    用于定义内部各步骤.

    `steps` is a list of dicts with keys:

    - description (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的详情描述内容.

    - icon (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的图标内容.

    - status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
        用于指定当前步骤的状态  可选的有'wait'、'process'、'finish'、'error'
        当不设置时，会自动根据current来指定状态  默认：'wait'.

    - title (a list of or a singular dash component, string or number; optional):
        用于设置当前步骤的标题内容.

- current (number; default 0):
    用于设置当前步骤条所在步骤（从0开始计数）  默认：0.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    用于设置步骤条显示方向  可选的有'horizontal'、'vertical'  默认：'horizontal'."""
    _children_props = ['steps[].description', 'steps[].icon', 'steps[].title']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSteps'
    Steps = TypedDict(
        "Steps",
            {
            "description": NotRequired[ComponentType],
            "icon": NotRequired[ComponentType],
            "status": NotRequired[Literal["wait", "process", "finish", "error"]],
            "title": NotRequired[ComponentType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        steps: typing.Optional[typing.Sequence["Steps"]] = None,
        current: typing.Optional[NumberType] = None,
        direction: typing.Optional[Literal["horizontal", "vertical"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'steps', 'current', 'direction']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'steps', 'current', 'direction']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileSteps, self).__init__(**args)

setattr(MobileSteps, "__init__", _explicitize_args(MobileSteps.__init__))
