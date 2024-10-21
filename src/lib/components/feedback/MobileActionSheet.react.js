/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { ActionSheet } from 'antd-mobile';

/**
 * 动作面板组件MobileActionSheet
 */
const MobileActionSheet = (props) => {
    let {
        id,
        style,
        className,
        actions,
        cancelText,
        closeOnAction,
        closeOnMaskClick,
        destroyOnClose,
        forceRender,
        extra,
        popupClassName,
        safeArea,
        visible,
        styles,
        loading_state,
        setProps
    } = props;

    return <ActionSheet
        id={id}
        style={style}
        className={className}
        actions={actions}
        cancelText={cancelText}
        closeOnAction={closeOnAction}
        closeOnMaskClick={closeOnMaskClick}
        destroyOnClose={destroyOnClose}
        forceRender={forceRender}
        extra={extra}
        popupClassName={popupClassName}
        safeArea={safeArea}
        visible={visible}
        styles={styles}
        onClose={() => setProps({ visible: false })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileActionSheet.propTypes = {
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
     * 配置面板选项
     */
    actions: PropTypes.arrayOf(
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
             * 当前选项描述信息
             */
            description: PropTypes.string,
            /**
             * 是否禁用当前选项
             * 默认值：`false`
             */
            disabled: PropTypes.bool,
            /**
             * 当前选项是否渲染为危险状态
             * 默认值：`false`
             */
            danger: PropTypes.bool,
            /**
             * 当前选项标题是否加粗
             * 默认值：`false`
             */
            bold: PropTypes.bool
        })
    ),

    /**
     * 组件型，取消按钮内容，不设置时不显示取消按钮
     */
    cancelText: PropTypes.node,

    /**
     * 点击选项后是否自动关闭面板
     * 默认值：`false`
     */
    closeOnAction: PropTypes.bool,

    /**
     * 是否可通过点击背景蒙版层关闭面板
     * 默认值：`true`
     */
    closeOnMaskClick: PropTypes.bool,

    /**
     * 面板不可见时是否销毁内部元素
     * 默认值：`false`
     */
    destroyOnClose: PropTypes.bool,

    /**
     * 是否强制渲染内部元素
     * 默认值：`false`
     */
    forceRender: PropTypes.bool,

    /**
     * 组件型，顶部额外内容
     */
    extra: PropTypes.node,

    /**
     * 弹出层css类名
     */
    popupClassName: PropTypes.string,

    /**
     * 是否开启安全区适配
     * 默认值：`true`
     */
    safeArea: PropTypes.bool,

    /**
     * 监听或设置当前面板显示状态
     * 默认值：`false`
     */
    visible: PropTypes.bool,

    /**
     * 语义化结构css样式
     */
    styles: PropTypes.exact({
        /**
         * 内容区css样式
         */
        body: PropTypes.object,
        /**
         * 背景蒙版层css样式
         */
        mask: PropTypes.object
    }),

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

MobileActionSheet.defaultProps = {
    closeOnAction: false,
    closeOnMaskClick: true,
    destroyOnClose: false,
    forceRender: false,
    safeArea: true,
    visible: false
};

export default React.memo(MobileActionSheet);