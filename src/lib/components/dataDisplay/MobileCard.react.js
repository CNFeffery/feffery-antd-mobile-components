/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Card } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 卡片组件MobileCard
 */
const MobileCard = ({
    id,
    key,
    style,
    className,
    children,
    bodyClassName,
    bodyStyle,
    extra,
    headerClassName,
    headerStyle,
    title,
    setProps
}) => {

    return <Card
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        bodyClassName={bodyClassName}
        bodyStyle={bodyStyle}
        extra={extra}
        headerClassName={headerClassName}
        headerStyle={headerStyle}
        title={title}
        data-dash-is-loading={useLoading()}
    />;
};

MobileCard.propTypes = {
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
     * 用于设置当前卡片body区域css类
     */
    bodyClassName: PropTypes.string,

    /**
     * 用于设置当前卡片body区域css样式
     */
    bodyStyle: PropTypes.object,

    /**
     * 用于为当前卡片设置头部右侧元素
     */
    extra: PropTypes.node,

    /**
     * 用于设置当前卡片头部区域css类
     */
    headerClassName: PropTypes.string,

    /**
     * 用于设置当前卡片头部区域css样式
     */
    headerStyle: PropTypes.object,

    /**
     * 用于为当前卡片设置头部左侧标题内容
     */
    title: PropTypes.node,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileCard);