/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Grid } from 'antd-mobile';
import { useLoading } from '../../utils';

/**
 * 栅格项组件MobileGridItem
 */
const MobileGridItem = ({
    id,
    key,
    style,
    className,
    children,
    span = 1,
    setProps
}) => {

    return <Grid.Item
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        span={span}
        data-dash-is-loading={useLoading()}
    />;
};

MobileGridItem.propTypes = {
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
     * 用于设置当前栅格项在对应栅格中所占的份数
     * 默认：1
     */
    span: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileGridItem);