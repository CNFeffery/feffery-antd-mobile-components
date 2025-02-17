/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Button } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';

/**
 * 按钮组件MobileButton
 */
const MobileButton = ({
    id,
    style,
    className,
    children,
    block = false,
    color = 'default',
    disabled = false,
    fill = 'solid',
    loading = false,
    loadingText,
    shape = 'default',
    size = 'middle',
    type = 'button',
    nClicks = 0,
    setProps
}) => {

    return <Button
        id={id}
        style={style}
        className={className}
        children={children}
        block={block}
        color={color}
        disabled={disabled}
        fill={fill}
        loading={loading}
        loadingText={loadingText}
        shape={shape}
        size={size}
        type={type}
        onClick={() => setProps({ nClicks: nClicks + 1 })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileButton.propTypes = {
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
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前按钮是否撑满父元素
     * 默认值：`false`
     */
    block: PropTypes.bool,

    /**
     * 按钮颜色状态，可选项有`'default'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
     * 默认值：`'default'`
     */
    color: PropTypes.oneOf(['default', 'primary', 'success', 'warning', 'danger']),

    /**
     * 是否禁用当前按钮
     * 默认值：`false`
     */
    disabled: PropTypes.bool,

    /**
     * 当前按钮填充模式，可选项有`'solid'`、`'outline'`、`'none'`
     * 默认值：`'solid'`
     */
    fill: PropTypes.oneOf(['solid', 'outline', 'none']),

    /**
     * 当前按钮是否处于加载中状态
     * 默认值：`false`
     */
    loading: PropTypes.bool,

    /**
     * 加载中状态下额外展示的文字内容
     */
    loadingText: PropTypes.string,

    /**
     * 用于设置当前按钮的形状，可选项有`'default'`、`'rounded'`、`'rectangular'`
     * 默认值：`'default'`
     */
    shape: PropTypes.oneOf(['default', 'rounded', 'rectangular']),

    /**
     * 用于设置当前按钮的尺寸规格，可选项有`'mini'`、`'small'`、`'middle'`、`'large'`
     * 默认值：`'middle'`
     */
    size: PropTypes.oneOf(['mini', 'small', 'middle', 'large']),

    /**
     * 用于设置当前按钮对应原生`html`的`type`属性，可选项有`'submit'`、`'reset'`、`'button'`
     * 默认值：`'button'`
     */
    type: PropTypes.oneOf(['submit', 'reset', 'button']),

    /**
     * 监听当前按钮累计被点击次数
     * 默认值：`0`
     */
    nClicks: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileButton);