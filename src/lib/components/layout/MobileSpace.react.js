/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Space } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 间距组件MobileSpace
 */
const MobileSpace = ({
    id,
    key,
    style,
    className,
    children,
    align,
    block = false,
    direction = 'horizontal',
    justify,
    wrap = false,
    setProps
}) => {

    return <Space
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        align={align}
        block={block}
        direction={direction}
        justify={justify}
        wrap={wrap}
        data-dash-is-loading={useLoading()}
    />;
};

MobileSpace.propTypes = {
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
     * 用于设置当前间距组件的交叉轴对齐方式
     * 可选的有'start'、'end'、'center'、'baseline'
     */
    align: PropTypes.oneOf(['start', 'end', 'center', 'baseline']),

    /**
     * 用于设置当前间距组件是否撑满父元素
     * 默认：false
     */
    block: PropTypes.bool,

    /**
     * 用于设置当前间距组件的方向
     * 可选的有'vertical'、'horizontal'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 用于设置当前间距组件的主轴对齐方式
     * 可选的有'start'、'end'、'center'、'between'、'around'、'evenly'、'stretch'
     */
    justify: PropTypes.oneOf(['start', 'end', 'center', 'between', 'around', 'evenly', 'stretch']),

    /**
     * 用于设置当前间距组件是否自动换行，仅在'horizontal'方向下有效
     * 默认：false
     */
    wrap: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileSpace);