/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { CenterPopup } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 居中弹出层组件MobileCenterPopup
 */
const MobileCenterPopup = ({
    id,
    key,
    style,
    className,
    children,
    visible = false,
    bodyClassName,
    bodyStyle,
    closeOnMaskClick = false,
    destroyOnClose = false,
    forceRender = false,
    mask = true,
    maskClassName,
    maskStyle,
    showCloseButton,
    closeOnSwipe = false,
    setProps
}) => {

    return <CenterPopup
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        visible={visible}
        bodyClassName={bodyClassName}
        bodyStyle={bodyStyle}
        closeOnMaskClick={closeOnMaskClick}
        destroyOnClose={destroyOnClose}
        forceRender={forceRender}
        mask={mask}
        maskClassName={maskClassName}
        maskStyle={maskStyle}
        showCloseButton={showCloseButton}
        closeOnSwipe={closeOnSwipe}
        onClose={() => setProps({ visible: false })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileCenterPopup.propTypes = {
    // 通用参数
    /**
     * 用于设置当前组件唯一id
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于为当前弹出层容器设置css样式
     */
    style: PropTypes.object,

    /**
     * 用于为当前弹出层容器设置css类名
     */
    className: PropTypes.string,

    /**
     * 用于设置内部元素
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 用于设置或监听当前弹出层是否展开
     * 默认：false
     */
    visible: PropTypes.bool,

    /**
     * 用于设置内容区域css类
     */
    bodyClassName: PropTypes.string,

    /**
     * 用于设置内容区域css样式
     */
    bodyStyle: PropTypes.object,

    /**
     * 用于设置点击背景蒙板层是否可关闭当前弹出层
     * 默认：false
     */
    closeOnMaskClick: PropTypes.bool,

    /**
     * 用于设置当前弹出层内部元素是否在关闭时自动销毁
     * 默认：false
     */
    destroyOnClose: PropTypes.bool,

    /**
     * 用于设置初始化时是否强制销毁内部元素
     * 默认：false
     */
    forceRender: PropTypes.bool,

    /**
     * 用于设置是否展示蒙板层
     * 默认：true
     */
    mask: PropTypes.bool,

    /**
     * 用于设置蒙板层css类
     */
    maskClassName: PropTypes.string,

    /**
     * 用于设置蒙板层css样式
     */
    maskStyle: PropTypes.object,

    /**
     * 用于设置是否渲染关闭按钮
     * 默认：false
     */
    showCloseButton: PropTypes.bool,

    /**
     * 用于设置是否支持上/下滑动关闭弹出层
     * 默认：false
     */
    closeOnSwipe: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileCenterPopup);