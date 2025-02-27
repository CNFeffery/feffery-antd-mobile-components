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
import { useLoading } from '../../../utils';


/**
 * 表单项组件MobileFormItem
 */
const MobileFormItem = ({
    id,
    key,
    style,
    className,
    children,
    childElementPosition = 'normal',
    disabled,
    help,
    hidden = false,
    label,
    layout,
    required = false,
    setProps
}) => {

    return <Form.Item
        id={id}
        key={key}
        style={style}
        className={className}
        childElementPosition={childElementPosition}
        disabled={disabled}
        help={help}
        hidden={hidden}
        label={label}
        layout={layout}
        required={required}
        children={children}
        data-dash-is-loading={useLoading()}
    />;
};


MobileFormItem.propTypes = {
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
     * 表单项控件的位置，可选的有'normal'、'right'
     * 默认：'normal'
     */
    childElementPosition: PropTypes.oneOf(['normal', 'right']),

    /**
     * 是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 额外提示信息
     */
    help: PropTypes.node,

    /**
     * 是否隐藏当前表单项
     * 默认：false
     */
    hidden: PropTypes.bool,

    /**
     * 标签内容
     */
    label: PropTypes.node,

    /**
     * 自定义布局模式，可选的有'vertical'、'horizontal'
     * 默认以父级表单组件的布局模式为准
     */
    layout: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 是否显示必选标记
     * 默认：false
     */
    required: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileFormItem);