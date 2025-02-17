/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Divider } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 分割线组件MobileDivider
 */
const MobileDivider = ({
    id,
    key,
    style,
    className,
    children,
    contentPosition = 'center',
    direction = 'horizontal',
    setProps
}) => {

    return <Divider
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        contentPosition={contentPosition}
        direction={direction}
        data-dash-is-loading={useLoading()}
    />;
};

MobileDivider.propTypes = {
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
     * 用于设置当前分割线中内容的位置，仅在水平方向展示时有效
     * 可选的有'center'、'left'、'right'
     * 默认：'center'
     */
    contentPosition: PropTypes.oneOf(['center', 'left', 'right']),

    /**
     * 用于设置当前分割线的展示方向
     * 可选的有'horizontal'、'vertical'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileDivider);