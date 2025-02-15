/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Result } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 结果组件MobileResult
 */
const MobileResult = ({
    id,
    key,
    style,
    className,
    description,
    icon,
    status = 'info',
    title,
    setProps
}) => {

    return <Result
        id={id}
        key={key}
        style={style}
        className={className}
        description={description}
        icon={icon}
        status={status}
        title={title}
        data-dash-is-loading={useLoading()}
    />;
};


MobileResult.propTypes = {
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
     * 描述信息
     */
    description: PropTypes.node,

    /**
     * 自定义图标
     */
    icon: PropTypes.node,

    /**
     * 状态类型，可选的有'success'、'error'、'info'、'waiting'、'warning'
     * 默认：'info'
     */
    status: PropTypes.oneOf(['success', 'error', 'info', 'waiting', 'warning']),

    /**
     * 标题信息
     */
    title: PropTypes.node,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileResult);