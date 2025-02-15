/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { FloatingBubble } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 浮动气泡组件MobileFloatingBubble
 */
const MobileFloatingBubble = ({
    id,
    key,
    style,
    className,
    children,
    axis = 'y',
    magnetic,
    offset,
    nClicks = 0,
    setProps
}) => {

    return <FloatingBubble
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        axis={axis}
        magnetic={magnetic}
        offset={{
            x: 0,
            y: 0,
            ...offset
        }}
        onOffsetChange={(e) => setProps({ offset: e })}
        onClick={() => setProps({ nClicks: nClicks + 1 })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileFloatingBubble.propTypes = {
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

    /**
     * 设置可进行拖动的方向，可选的有'xy'（自由拖动）、'lock'（仅允许在开始拖拽时的方向上进行拖拽）、'x'（仅允许在水平方向上进行拖拽）、'y'（仅允许在垂直方向上进行拖拽）
     * 默认：'y'
     */
    axis: PropTypes.oneOf(['xy', 'lock', 'x', 'y']),

    /**
     * 设置自动磁吸的方向，可选的有'x'、'y'，默认不开启磁吸效果
     */
    magnetic: PropTypes.oneOf(['x', 'y']),

    /**
     * 监听或设置像素偏移位置
     */
    offset: PropTypes.exact({
        /**
         * 水平方向像素偏移位置
         * 默认：0
         */
        x: PropTypes.number,
        /**
         * 垂直方向像素偏移位置
         * 默认：0
         */
        y: PropTypes.number
    }),

    /**
     * 监听当前浮动气泡组件累计被点击次数
     * 默认：0
     */
    nClicks: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileFloatingBubble);