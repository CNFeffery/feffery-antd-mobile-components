/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { ResultPage } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 结果页面组件MobileResultPage
 */
const MobileResultPage = ({
    id,
    style,
    className,
    children,
    title,
    description,
    icon,
    details,
    status = 'info',
    primaryButtonText,
    secondaryButtonText,
    nClicksPrimary = 0,
    nClicksSecondary = 0,
    setProps
}) => {

    return <ResultPage
        id={id}
        style={style}
        className={className}
        children={children}
        title={title}
        description={description}
        icon={icon}
        details={details}
        status={status}
        primaryButtonText={primaryButtonText}
        secondaryButtonText={secondaryButtonText}
        onPrimaryButtonClick={() => setProps({ nClicksPrimary: nClicksPrimary + 1 })}
        onSecondaryButtonClick={() => setProps({ nClicksSecondary: nClicksSecondary + 1 })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileResultPage.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 组件型，内嵌元素，推荐配合`MobileResultPageCard`
     */
    children: PropTypes.node,

    /**
     * 组件型，结果标题信息
     */
    title: PropTypes.node,

    /**
     * 组件型，结果描述信息
     */
    description: PropTypes.node,

    /**
     * 组件型，结果标题内容
     */
    icon: PropTypes.node,

    /**
     * 配置结果页详情信息项
     */
    details: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 组件型，当前信息项标题
             */
            label: PropTypes.node,
            /**
             * 组件型，当前信息项内容
             */
            value: PropTypes.node,
            /**
             * 当前信息项是否加粗
             * 默认值：`false`
             */
            bold: PropTypes.bool
        })
    ),

    /**
     * 结果页状态类型，可选项有`'success'`、`'error'`、`'info'`、`'waiting'`、`'warning'`
     * 默认值：`'info'`
     */
    status: PropTypes.oneOf(['success', 'error', 'info', 'waiting', 'warning']),

    /**
     * 主要操作按钮内嵌内容，传入空值时不显示主要按钮
     */
    primaryButtonText: PropTypes.node,

    /**
     * 辅助操作按钮内嵌内容，传入空值时不显示辅助操作按钮
     */
    secondaryButtonText: PropTypes.node,

    /**
     * 监听主要操作按钮累计点击次数
     * 默认值：`0`
     */
    nClicksPrimary: PropTypes.number,

    /**
     * 监听辅助操作按钮累计点击次数
     * 默认值：`0`
     */
    nClicksSecondary: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileResultPage);