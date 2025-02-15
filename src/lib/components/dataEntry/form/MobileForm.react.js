/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Form } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 表单组件MobileForm
 */
const MobileForm = ({
    id,
    key,
    style,
    className,
    children,
    disabled = false,
    footer,
    layout = 'vertical',
    mode = 'default',
    requiredMarkStyle = 'asterisk',
    setProps
}) => {

    return <Form
        id={id}
        key={key}
        style={style}
        className={className}
        disabled={disabled}
        footer={footer}
        layout={layout}
        mode={mode}
        requiredMarkStyle={requiredMarkStyle}
        children={children}
        data-dash-is-loading={useLoading()}
    />;
};


MobileForm.propTypes = {
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
     * 用于传入内部各MobileFormItem表单项组件
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 自定义表单底部元素
     */
    footer: PropTypes.node,

    /**
     * 布局模式，可选的有'vertical'、'horizontal'
     * 默认：'vertical'
     */
    layout: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 渲染模式，可选的有'default'、'card'
     * 默认：'default'
     */
    mode: PropTypes.oneOf(['default', 'card']),

    /**
     * 针对内部表单项的必填选填标记样式类型进行设置
     * 可选的有'asterisk'、'text-required'、'text-optional'、'none'
     * 默认：'asterisk'
     */
    requiredMarkStyle: PropTypes.oneOf(['asterisk', 'text-required', 'text-optional', 'none']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileForm);