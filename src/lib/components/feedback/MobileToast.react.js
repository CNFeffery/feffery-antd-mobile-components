/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Toast } from 'antd-mobile';

/**
 * 轻提示组件MobileToast
 */
const MobileToast = (props) => {
    let {
        content,
        duration,
        icon,
        maskClassName,
        maskClickable,
        maskStyle,
        position,
        loading_state,
        setProps
    } = props;

    useEffect(() => {
        Toast.show({
            content,
            duration,
            icon,
            maskClassName,
            maskClickable,
            maskStyle,
            position
        })
    })

    return <></>
};


MobileToast.propTypes = {
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
     * 用于为当前组件设置css样式
     */
    style: PropTypes.object,

    /**
     * 用于为当前组件设置css类名
     */
    className: PropTypes.string,

    // 组件常规参数
    /**
     * 轻提示内容
     */
    content: PropTypes.node,

    /**
     * 持续显示时长，单位：毫秒
     * 默认：2000
     */
    duration: PropTypes.number,

    /**
     * 额外图标类型，可选的有'success'、'fail'、'loading'
     */
    icon: PropTypes.oneOf(['success', 'fail', 'loading']),

    /**
     * 遮罩层css类名
     */
    maskClassName: PropTypes.string,

    /**
     * 背景是否可点击
     * 默认：true
     */
    maskClickable: PropTypes.bool,

    /**
     * 遮罩层css样式
     */
    maskStyle: PropTypes.object,

    /**
     * 垂直方向显示位置，可选的有'top'、'bottom'、'center'
     * 默认：'center'
     */
    position: PropTypes.oneOf(['top', 'bottom', 'center']),

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

MobileToast.defaultProps = {
    duration: 2000,
    maskClickable: true,
    position: 'center'
};

export default React.memo(MobileToast);