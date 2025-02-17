/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { ProgressCircle } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 进度圈组件MobileProgressCircle
 */
const MobileProgressCircle = ({
    id,
    key,
    style,
    className,
    children,
    percent = 0,
    setProps
}) => {

    return <ProgressCircle
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        percent={percent}
        data-dash-is-loading={useLoading()}
    />;
};

MobileProgressCircle.propTypes = {
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
     * 设置进度圈百分比，取值应在0到100之间
     * 默认：0
     */
    percent: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileProgressCircle);