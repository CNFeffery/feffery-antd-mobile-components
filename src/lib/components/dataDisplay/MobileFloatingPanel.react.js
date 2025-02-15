/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { FloatingPanel } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 浮动面板组件MobileFloatingPanel
 */
const MobileFloatingPanel = ({
    id,
    key,
    style,
    className,
    children,
    anchors = [100, 0.5],
    handleDraggingOfContent = true,
    setProps
}) => {

    return <FloatingPanel
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        anchors={
            anchors.map(
                (anchor) => {
                    if (anchor <= 1) {
                        return window.innerHeight * anchor
                    }
                    return anchor
                }
            )
        }
        handleDraggingOfContent={handleDraggingOfContent}
        data-dash-is-loading={useLoading()}
    />;
};

MobileFloatingPanel.propTypes = {
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
     * 用于设置内部元素
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 用于设置当前浮动面板可拖拽至哪些高度，单位：px
     * 特别地，当传入值在0到1（包含1）之间时，会自动根据当前页面整体高度进行比例计算
     * 默认：[100, 0.5]
     */
    anchors: PropTypes.arrayOf(PropTypes.number),

    /**
     * 用于设置面板内部元素是否也可被拖拽以移动面板
     * 默认：true
     */
    handleDraggingOfContent: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileFloatingPanel);