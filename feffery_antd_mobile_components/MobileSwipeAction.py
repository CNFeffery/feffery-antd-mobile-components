# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileSwipeAction(Component):
    """A MobileSwipeAction component.
滑动操作组件MobileSwipeAction

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- children (a list of or a singular dash component, string or number; optional):
    用于设置触发目标元素.

- closeOnAction (boolean; default True):
    是否在点击操作按钮后自动归位  默认值：`True`.

- closeOnTouchOutside (boolean; default True):
    是否在点击其他区域时自动归位  默认值：`True`.

- leftActions (list of dicts; optional):
    配置左侧的操作按钮列表.

    `leftActions` is a list of dicts with keys:

    - key (string | number; optional):
        当前操作按钮唯一标识.

    - color (string; optional):
        当前操作按钮颜色，可设置`css`中合法的颜色值，内置的颜色有`'light'`、`'weak'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
        默认值：`'light'`.

    - text (a list of or a singular dash component, string or number; optional):
        当前操作按钮内容.

- rightActions (list of dicts; optional):
    配置右侧的操作按钮列表.

    `rightActions` is a list of dicts with keys:

    - color (string; optional):
        当前操作按钮颜色，可设置`css`中合法的颜色值，内置的颜色有`'light'`、`'weak'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
        默认值：`'light'`.

    - key (string | number; optional):
        当前操作按钮唯一标识.

    - text (a list of or a singular dash component, string or number; optional):
        当前操作按钮内容.

- actionEvent (dict; optional):
    监听最近一次操作按钮点击事件.

    `actionEvent` is a dict with keys:

    - key (string | number; optional):
        操作按钮对应`key`值.

    - timestamp (number; optional):
        事件对应时间戳.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['leftActions[].text', 'rightActions[].text']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileSwipeAction'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, closeOnAction=Component.UNDEFINED, closeOnTouchOutside=Component.UNDEFINED, leftActions=Component.UNDEFINED, rightActions=Component.UNDEFINED, actionEvent=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'closeOnAction', 'closeOnTouchOutside', 'leftActions', 'rightActions', 'actionEvent', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'closeOnAction', 'closeOnTouchOutside', 'leftActions', 'rightActions', 'actionEvent', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobileSwipeAction, self).__init__(children=children, **args)
