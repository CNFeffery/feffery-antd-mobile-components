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

/**
 * 表单分组标题组件MobileFormHeader
 */
const MobileFormHeader = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        loading_state,
        setProps
    } = props;

    return <Form.Header
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};


MobileFormHeader.propTypes = {
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
     * 用于传入标签内容
     */
    children: PropTypes.node,

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

MobileFormHeader.defaultProps = {
};

export default React.memo(MobileFormHeader);