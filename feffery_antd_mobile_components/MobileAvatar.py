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


class MobileAvatar(Component):
    """A MobileAvatar component.
头像组件MobileAvatar

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- className (string; optional):
    用于为当前组件设置css类名.

- children (a list of or a singular dash component, string or number; optional):
    用于设置内部元素.

- fallback (a list of or a singular dash component, string or number; optional):
    用于为当前头像组件设置默认占位图.

- fit (a value equal to: 'contain', 'cover', 'fill', 'none', 'scale-down'; default 'cover'):
    用于为当前头像组件设置图片填充模式
    可选的有'contain'、'cover'、'fill'、'none'、'scale-down'  默认：'cover'.

- src (string; default ''):
    用于为当前头像组件设置图片地址.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['fallback']
    _base_nodes = ['fallback', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileAvatar'
    LoadingState = TypedDict(
        "LoadingState",
            {
            "is_loading": NotRequired[bool],
            "prop_name": NotRequired[str],
            "component_name": NotRequired[str]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        fallback: typing.Optional[ComponentType] = None,
        fit: typing.Optional[Literal["contain", "cover", "fill", "none", "scale-down"]] = None,
        src: typing.Optional[str] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'children', 'fallback', 'fit', 'src', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'children', 'fallback', 'fit', 'src', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileAvatar, self).__init__(children=children, **args)

setattr(MobileAvatar, "__init__", _explicitize_args(MobileAvatar.__init__))
