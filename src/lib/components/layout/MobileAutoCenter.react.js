/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { AutoCenter } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 自动居中组件MobileAutoCenter
 */
const MobileAutoCenter = ({
    id,
    key,
    style,
    className,
    children,
    setProps
}) => {

    return <AutoCenter
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        data-dash-is-loading={useLoading()}
    />;
};

MobileAutoCenter.propTypes = {
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
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileAutoCenter);