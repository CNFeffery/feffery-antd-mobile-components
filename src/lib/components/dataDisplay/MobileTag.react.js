/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Tag } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 标签组件MobileTag
 */
const MobileTag = ({
    id,
    key,
    style,
    className,
    children,
    color = 'default',
    fill = 'solid',
    round = false,
    setProps
}) => {

    return <Tag
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        color={color}
        fill={fill}
        round={round}
        data-dash-is-loading={useLoading()}
    />;
};

MobileTag.propTypes = {
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
     * 用于为当前标签设置颜色
     * 内置的状态色有'default'、'primary'、'success'、'warning'、'danger'
     * 也可传入css中合法的色彩值作为自定义颜色
     * 默认：'default'
     */
    color: PropTypes.oneOfType([
        PropTypes.oneOf(['default', 'primary', 'success', 'warning', 'danger']),
        PropTypes.string
    ]),

    /**
     * 用于为当前标签设置填充模式
     * 可选的有'solid'、'outline'
     * 默认：'solid'
     */
    fill: PropTypes.oneOf(['solid', 'outline']),

    /**
     * 用于为当前标签设置是否开启圆角
     * 默认：false
     */
    round: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileTag);