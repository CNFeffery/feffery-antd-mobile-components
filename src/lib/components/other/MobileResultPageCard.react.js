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

/**
 * 结果页面卡片组件MobileResultPageCard
 */
const MobileResultPageCard = (props) => {
    let {
        id,
        style,
        className,
        children,
        loading_state,
        setProps
    } = props;

    return <ResultPage.Card
        id={id}
        style={style}
        className={className}
        children={children}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileResultPageCard.propTypes = {
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

MobileResultPageCard.defaultProps = {
};

export default React.memo(MobileResultPageCard);