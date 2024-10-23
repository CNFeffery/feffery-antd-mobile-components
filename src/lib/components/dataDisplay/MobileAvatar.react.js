/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Avatar } from 'antd-mobile';

/**
 * 头像组件MobileAvatar
 */
const MobileAvatar = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        fallback,
        fit,
        src,
        loading_state,
        setProps
    } = props;

    return <Avatar
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        fallback={fallback}
        fit={fit}
        src={src}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileAvatar.propTypes = {
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
     * 用于为当前头像组件设置默认占位图
     */
    fallback: PropTypes.node,

    /**
     * 用于为当前头像组件设置图片填充模式
     * 可选的有'contain'、'cover'、'fill'、'none'、'scale-down'
     * 默认：'cover'
     */
    fit: PropTypes.oneOf(['contain', 'cover', 'fill', 'none', 'scale-down']),

    /**
     * 用于为当前头像组件设置图片地址
     */
    src: PropTypes.string,

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

MobileAvatar.defaultProps = {
    fit: 'cover',
    src: ''
};

export default React.memo(MobileAvatar);