/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { NavBar } from 'antd-mobile';

/**
 * 导航栏组件MobileNavBar
 */
const MobileNavBar = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        back,
        backArrow,
        left,
        right,
        nBackClicks,
        loading_state,
        setProps
    } = props;

    return <NavBar
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        back={back}
        backArrow={backArrow}
        left={left}
        right={right}
        onBack={() => setProps({ nBackClicks: nBackClicks + 1 })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileNavBar.propTypes = {
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
     * 用于设置导航栏标题内容
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 用于为当前导航栏设置返回区域文字内容，传入None时会连带返回按钮一起隐藏
     * 默认：''
     */
    back: PropTypes.node,

    /**
     * 用于为当前导航栏设置是否显示返回箭头，也可传入组件型输入充当自定义返回箭头
     * 默认：true
     */
    backArrow: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.node
    ]),

    /**
     * 用于设置显示在当前导航栏标题左侧的内容
     */
    left: PropTypes.node,

    /**
     * 用于设置显示在当前导航栏标题右侧的内容
     */
    right: PropTypes.node,

    // 组件监听类属性
    /**
     * 用于记录当前导航栏返回区域累计被点击次数
     */
    nBackClicks: PropTypes.number,

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

MobileNavBar.defaultProps = {
    back: '',
    backArrow: true,
    nBackClicks: 0
};

export default React.memo(MobileNavBar);