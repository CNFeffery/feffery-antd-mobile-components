# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobilePullToRefresh(Component):
    """A MobilePullToRefresh component.
下拉刷新组件MobilePullToRefresh

Keyword arguments:

- id (string; optional):
    用于设置当前组件唯一id.

- key (string; optional):
    强制重绘当前组件时使用.

- children (a list of or a singular dash component, string or number; optional):
    用于设置触发目标元素.

- canReleaseText (a list of or a singular dash component, string or number; optional):
    组件型，设置释放的提示文案.

- completeDelay (number; default 500):
    每次下拉刷新操作后，延迟消失时长，单位：毫秒  默认值：`500`.

- completeText (a list of or a singular dash component, string or number; optional):
    组件型，设置完成时的提示文案.

- disabled (boolean; default False):
    是否禁用下拉刷新功能  默认值：`False`.

- headHeight (number; default 40):
    头部提示内容区像素高度  默认值：`40`.

- pullingText (a list of or a singular dash component, string or number; optional):
    组件型，设置下拉的提示文案.

- refreshingText (a list of or a singular dash component, string or number; optional):
    组件型，刷新时的提示文案.

- threshold (number; default 60):
    触发刷新对应的最小下拉像素距离  默认值：`60`.

- refreshCount (number; default 0):
    监听下拉刷新操作累计触发次数  默认值：`0`.

- stopRefreshing (boolean; optional):
    用于手动终止进行中的加载过程，每次调用会将更新为`True`后，都会在终止加载状态后，被重置为`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['canReleaseText', 'completeText', 'pullingText', 'refreshingText']
    _base_nodes = ['canReleaseText', 'completeText', 'pullingText', 'refreshingText', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobilePullToRefresh'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, canReleaseText=Component.UNDEFINED, completeDelay=Component.UNDEFINED, completeText=Component.UNDEFINED, disabled=Component.UNDEFINED, headHeight=Component.UNDEFINED, pullingText=Component.UNDEFINED, refreshingText=Component.UNDEFINED, threshold=Component.UNDEFINED, refreshCount=Component.UNDEFINED, stopRefreshing=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'canReleaseText', 'completeDelay', 'completeText', 'disabled', 'headHeight', 'pullingText', 'refreshingText', 'threshold', 'refreshCount', 'stopRefreshing', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'canReleaseText', 'completeDelay', 'completeText', 'disabled', 'headHeight', 'pullingText', 'refreshingText', 'threshold', 'refreshCount', 'stopRefreshing', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MobilePullToRefresh, self).__init__(children=children, **args)
