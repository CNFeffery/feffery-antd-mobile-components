# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MobileDialog(Component):
    """A MobileDialog component.
对话框组件MobileDialog

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- actions (list of dicts; optional):
    配置操作按钮，可传入二级数组实现同一行并排显示多个按钮.

    `actions` is a list of dicts with keys:

    - key (string; required):
        必填，当前选项唯一标识.

    - text (string; required):
        必填，当前选项标题.

    - style (dict; optional):
        当前选项css样式.

    - className (string; optional):
        当前选项css类名.

    - bold (boolean; optional):
        当前选项文字是否加粗  默认值：`False`.

    - danger (boolean; optional):
        当前选项是否渲染为危险状态  默认值：`False`.

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`. | list of dicts with keys:

    - key (string; required):
        必填，当前选项唯一标识.

    - text (string; required):
        必填，当前选项标题.

    - style (dict; optional):
        当前选项css样式.

    - className (string; optional):
        当前选项css类名.

    - bold (boolean; optional):
        当前选项文字是否加粗  默认值：`False`.

    - danger (boolean; optional):
        当前选项是否渲染为危险状态  默认值：`False`.

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`.

- bodyClassName (string; optional):
    内容区css类名.

- bodyStyle (dict; optional):
    内容区css样式.

- closeOnAction (boolean; default False):
    点击操作按钮后是否自动关闭对话框  默认值：`False`.

- closeOnMaskClick (boolean; default False):
    是否可通过点击遮罩关闭对话框  默认值：`False`.

- content (a list of or a singular dash component, string or number; optional):
    组件型，对话框内容.

- destroyOnClose (boolean; default False):
    对话框不可见时是否销毁内部元素  默认值：`False`.

- disableBodyScroll (boolean; default True):
    是否禁用内容区滚动  默认值：`True`.

- forceRender (boolean; default False):
    是否强制渲染内部元素  默认值：`False`.

- header (a list of or a singular dash component, string or number; optional):
    组件型，对话框顶部区域内容.

- image (string; optional):
    内部图片地址.

- maskClassName (string; optional):
    遮罩层css类名.

- maskStyle (dict; optional):
    遮罩层css样式.

- title (a list of or a singular dash component, string or number; optional):
    组件型，对话框标题内容.

- visible (boolean; default False):
    监听或设置当前对话框是否显示  默认值：`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['content', 'header', 'title']
    _base_nodes = ['content', 'header', 'title', 'children']
    _namespace = 'feffery_antd_mobile_components'
    _type = 'MobileDialog'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, actions=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, bodyStyle=Component.UNDEFINED, closeOnAction=Component.UNDEFINED, closeOnMaskClick=Component.UNDEFINED, content=Component.UNDEFINED, destroyOnClose=Component.UNDEFINED, disableBodyScroll=Component.UNDEFINED, forceRender=Component.UNDEFINED, header=Component.UNDEFINED, image=Component.UNDEFINED, maskClassName=Component.UNDEFINED, maskStyle=Component.UNDEFINED, title=Component.UNDEFINED, visible=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'actions', 'bodyClassName', 'bodyStyle', 'closeOnAction', 'closeOnMaskClick', 'content', 'destroyOnClose', 'disableBodyScroll', 'forceRender', 'header', 'image', 'maskClassName', 'maskStyle', 'title', 'visible', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'actions', 'bodyClassName', 'bodyStyle', 'closeOnAction', 'closeOnMaskClick', 'content', 'destroyOnClose', 'disableBodyScroll', 'forceRender', 'header', 'image', 'maskClassName', 'maskStyle', 'title', 'visible', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MobileDialog, self).__init__(**args)
