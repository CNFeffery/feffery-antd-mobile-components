/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Popover } from 'antd-mobile';

/**
 * 气泡弹出框组件MobilePopover
 */
const MobilePopover = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        content,
        destroyOnHide,
        mode,
        placement,
        visible,
        loading_state,
        setProps
    } = props;

    return <Popover
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        content={content}
        destroyOnHide={destroyOnHide}
        mode={mode}
        placement={placement}
        visible={visible}
        trigger={'click'}
        onVisibleChange={(e) => setProps({ visible: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobilePopover.propTypes = {
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

    /**
     * 用于设置触发目标元素
     */
    children: PropTypes.node,

    /**
     * 设置气泡框内部元素
     */
    content: PropTypes.node,

    /**
     * 隐藏时，是否销毁气泡框内部元素
     * 默认：false
     */
    destroyOnHide: PropTypes.bool,

    /**
     * 设置显示模式，可选的有'light'、'dark'
     * 默认：'light'
     */
    mode: PropTypes.oneOf(['light', 'dark']),

    /**
     * 设置气泡框位置，可选的有'top'、'top-start'、'top-end'、'right'、'right-start'、'right-end'、'bottom'、'bottom-start'
     * 、'bottom-end'、'left'、'left-start'、'left-end'
     * 默认：'top'
     */
    placement: PropTypes.oneOf(['top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end']),

    /**
     * 监听或设置当前气泡框是否处于展开状态
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

MobilePopover.defaultProps = {
    destroyOnHide: false,
    mode: 'light',
    placement: 'top',
};

export default React.memo(MobilePopover);