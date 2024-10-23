/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { ErrorBlock } from 'antd-mobile';

/**
 * 异常组件MobileErrorBlock
 */
const MobileErrorBlock = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        description,
        fullPage,
        image,
        status,
        title,
        loading_state,
        setProps
    } = props;

    return <ErrorBlock
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        description={description}
        fullPage={fullPage}
        image={image}
        status={status}
        title={title}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileErrorBlock.propTypes = {
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
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 用于设置内部元素
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 额外描述信息
     */
    description: PropTypes.node,

    /**
     * 是否以整页模式进行渲染
     * 默认：false
     */
    fullPage: PropTypes.bool,

    /**
     * 自定义图片链接地址
     */
    image: PropTypes.string,

    /**
     * 预设状态类型，可选的有：'default', 'disconnected', 'empty', 'busy'
     * 默认：'default'
     */
    status: PropTypes.oneOf(['default', 'disconnected', 'empty', 'busy']),

    /**
     * 自定义标题信息
     */
    title: PropTypes.node,

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

MobileErrorBlock.defaultProps = {
    fullPage: false,
    status: 'default'
};

export default React.memo(MobileErrorBlock);