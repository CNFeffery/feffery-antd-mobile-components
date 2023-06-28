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

const MobileButton = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        block,
        color,
        disabled,
        fill,
        loading,
        loadingText,
        shape,
        size,
        type,
        nClicks,
        loading_state,
        setProps
    } = props;

    return <Button
        id={id}
        key={key}
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
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileButton.propTypes = {
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
     * 用于设置当前按钮是否撑满父元素
     * 默认：false
     */
    block: PropTypes.bool,

    /**
     * 用于设置按钮的颜色状态
     * 可选的有'default'、'primary'、'success'、'warning'、'danger'
     * 默认：'default'
     */
    color: PropTypes.oneOf(['default', 'primary', 'success', 'warning', 'danger']),

    /**
     * 用于设置是否禁用当前按钮
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 用于设置当前按钮的填充模式
     * 可选的有'solid'、'outline'、'none'
     * 默认：'solid'
     */
    fill: PropTypes.oneOf(['solid', 'outline', 'none']),

    /**
     * 用于设置当前按钮是否处于loading状态
     * 默认：false
     */
    loading: PropTypes.bool,

    /**
     * 用于设置loading状态下额外展示的文字内容
     */
    loadingText: PropTypes.string,

    /**
     * 用于设置当前按钮的形状
     * 可选的有'default'、'rounded'、'rectangular'
     * 默认：'default'
     */
    shape: PropTypes.oneOf(['default', 'rounded', 'rectangular']),

    /**
     * 用于设置当前按钮的尺寸规格
     * 可选的有'mini'、'small'、'middle'、'large'
     * 默认：'middle'
     */
    size: PropTypes.oneOf(['mini', 'small', 'middle', 'large']),

    /**
     * 用于设置当前按钮对应原生html的type属性
     * 可选的有'submit'、'reset'、'button'
     * 默认：'button'
     */
    type: PropTypes.oneOf(['submit', 'reset', 'button']),

    // 组件监听类属性
    /**
     * 用于记录当前按钮累计被点击次数
     */
    nClicks: PropTypes.number,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

MobileButton.defaultProps = {
    block: false,
    color: 'default',
    disabled: false,
    fill: 'solid',
    loading: false,
    shape: 'default',
    size: 'middle',
    type: 'button',
    nClicks: 0
};

export default React.memo(MobileButton);