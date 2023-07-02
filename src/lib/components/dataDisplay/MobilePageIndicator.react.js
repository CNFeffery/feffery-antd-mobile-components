/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { PageIndicator } from 'antd-mobile';

const MobilePageIndicator = (props) => {
    let {
        id,
        key,
        style,
        className,
        color,
        current,
        direction,
        total,
        loading_state,
        setProps
    } = props;

    return <PageIndicator
        id={id}
        key={key}
        style={style}
        className={className}
        color={color}
        current={current}
        direction={direction}
        total={total}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobilePageIndicator.propTypes = {
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

    // 组件常规参数
    /**
     * 用于设置当前分页符预设颜色方案
     * 可选的有'primary'、'white'
     * 默认：'primary'
     */
    color: PropTypes.oneOf(['primary', 'white']),

    /**
     * 用于设置当前分页符所在的页下标（从0开始计数）
     */
    current: PropTypes.number,

    /**
     * 用于设置当前分页符显示方向
     * 可选的有'horizontal'、'vertical'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * 用于设置当前分页符总页数
     */
    total: PropTypes.number,

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

MobilePageIndicator.defaultProps = {
    color: 'primary',
    direction: 'horizontal',
};

export default React.memo(MobilePageIndicator);