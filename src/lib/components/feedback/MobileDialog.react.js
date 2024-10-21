/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Dialog } from 'antd-mobile';

/**
 * 对话框组件MobileDialog
 */
const MobileDialog = (props) => {
    let {
        id,
        style,
        className,
        actions,
        bodyClassName,
        bodyStyle,
        closeOnAction,
        closeOnMaskClick,
        content,
        destroyOnClose,
        disableBodyScroll,
        forceRender,
        header,
        image,
        maskClassName,
        maskStyle,
        title,
        visible,
        loading_state,
        setProps
    } = props;

    return <Dialog
        id={id}
        style={style}
        className={className}
        actions={actions}
        bodyClassName={bodyClassName}
        bodyStyle={bodyStyle}
        closeOnAction={closeOnAction}
        closeOnMaskClick={closeOnMaskClick}
        content={content}
        destroyOnClose={destroyOnClose}
        disableBodyScroll={disableBodyScroll}
        forceRender={forceRender}
        header={header}
        image={image}
        maskClassName={maskClassName}
        maskStyle={maskStyle}
        title={title}
        visible={visible}
        onClose={() => setProps({ visible: false })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileDialog.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 配置操作按钮，可传入二级数组实现同一行并排显示多个按钮
     */
    actions: PropTypes.arrayOf(
        PropTypes.oneOfType([
            PropTypes.exact({
                /**
                 * 必填，当前选项唯一标识
                 */
                key: PropTypes.string.isRequired,
                /**
                 * 必填，当前选项标题
                 */
                text: PropTypes.string.isRequired,
                /**
                 * 当前选项css样式
                 */
                style: PropTypes.object,
                /**
                 * 当前选项css类名
                 */
                className: PropTypes.string,
                /**
                 * 当前选项文字是否加粗
                 * 默认值：`false`
                 */
                bold: PropTypes.bool,
                /**
                 * 当前选项是否渲染为危险状态
                 * 默认值：`false`
                 */
                danger: PropTypes.bool,
                /**
                 * 是否禁用当前选项
                 * 默认值：`false`
                 */
                disabled: PropTypes.bool
            }),
            PropTypes.arrayOf(
                PropTypes.exact({
                    /**
                     * 必填，当前选项唯一标识
                     */
                    key: PropTypes.string.isRequired,
                    /**
                     * 必填，当前选项标题
                     */
                    text: PropTypes.string.isRequired,
                    /**
                     * 当前选项css样式
                     */
                    style: PropTypes.object,
                    /**
                     * 当前选项css类名
                     */
                    className: PropTypes.string,
                    /**
                     * 当前选项文字是否加粗
                     * 默认值：`false`
                     */
                    bold: PropTypes.bool,
                    /**
                     * 当前选项是否渲染为危险状态
                     * 默认值：`false`
                     */
                    danger: PropTypes.bool,
                    /**
                     * 是否禁用当前选项
                     * 默认值：`false`
                     */
                    disabled: PropTypes.bool
                })
            )
        ])
    ),

    /**
     * 内容区css类名
     */
    bodyClassName: PropTypes.string,

    /**
     * 内容区css样式
     */
    bodyStyle: PropTypes.object,

    /**
     * 点击操作按钮后是否自动关闭对话框
     * 默认值：`false`
     */
    closeOnAction: PropTypes.bool,

    /**
     * 是否可通过点击遮罩关闭对话框
     * 默认值：`false`
     */
    closeOnMaskClick: PropTypes.bool,

    /**
     * 组件型，对话框内容
     */
    content: PropTypes.node,

    /**
     * 对话框不可见时是否销毁内部元素
     * 默认值：`false`
     */
    destroyOnClose: PropTypes.bool,

    /**
     * 是否禁用内容区滚动
     * 默认值：`true`
     */
    disableBodyScroll: PropTypes.bool,

    /**
     * 是否强制渲染内部元素
     * 默认值：`false`
     */
    forceRender: PropTypes.bool,

    /**
     * 组件型，对话框顶部区域内容
     */
    header: PropTypes.node,

    /**
     * 内部图片地址
     */
    image: PropTypes.string,

    /**
     * 遮罩层css类名
     */
    maskClassName: PropTypes.string,

    /**
     * 遮罩层css样式
     */
    maskStyle: PropTypes.object,

    /**
     * 组件型，对话框标题内容
     */
    title: PropTypes.node,

    /**
     * 监听或设置当前对话框是否显示
     * 默认值：`false`
     */
    visible: PropTypes.bool,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

MobileDialog.defaultProps = {
    closeOnAction: false,
    closeOnMaskClick: false,
    destroyOnClose: false,
    disableBodyScroll: true,
    forceRender: false,
    visible: false
};

export default React.memo(MobileDialog);