/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useState, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Skeleton } from 'antd-mobile';

/**
 * 骨架屏组件MobileSkeleton
 */
const MobileSkeleton = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        animated,
        debug,
        listenPropsMode,
        excludeProps,
        includeProps,
        loading_state,
        setProps
    } = props;

    const [showLoading, setShowLoading] = useState(false);
    const timer = useRef();

    useEffect(() => {
        if (loading_state) {
            if (timer.current) {
                clearTimeout(timer.current);
            }
            if (loading_state.is_loading && !showLoading) {
                // 当listenPropsMode为'default'时
                if (listenPropsMode === 'default') {
                    if (debug) {
                        console.log(loading_state.component_name + '.' + loading_state.prop_name)
                    }
                    setShowLoading(true);
                } else if (listenPropsMode === 'exclude') {
                    // 当listenPropsMode为'exclude'模式时
                    // 当前触发loading_state的组件+属性组合不在排除列表中时，激活动画
                    if (excludeProps.indexOf(loading_state.component_name + '.' + loading_state.prop_name) === -1) {
                        if (debug) {
                            console.log(loading_state.component_name + '.' + loading_state.prop_name)
                        }
                        setShowLoading(true);
                    }
                } else if (listenPropsMode === 'include') {
                    // 当listenPropsMode为'include'模式时
                    // 当前触发loading_state的组件+属性组合在包含列表中时，激活动画
                    if (includeProps.indexOf(loading_state.component_name + '.' + loading_state.prop_name) !== -1) {
                        if (debug) {
                            console.log(loading_state.component_name + '.' + loading_state.prop_name)
                        }
                        setShowLoading(true);
                    }
                }

            } else if (!loading_state.is_loading && showLoading) {
                timer.current = setTimeout(() => setShowLoading(false));
            }
        }
    }, [loading_state]);

    return (
        showLoading ?
            <Skeleton
                id={id}
                key={key}
                style={style}
                className={className}
                animated={animated}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
            /> :
            <>{children}</>
    )
};

MobileSkeleton._dashprivate_isLoadingComponent = true;

MobileSkeleton.propTypes = {
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
     * 是否开启动画效果
     * 默认：false
     */
    animated: PropTypes.bool,

    /**
     * 是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印prop信息
     * 默认：false
     */
    debug: PropTypes.bool,

    /**
     * 设置自定义监听组件的模式，可选的有'default'、'exclude'、'include'
     * 默认：'default'
     */
    listenPropsMode: PropTypes.oneOf(['default', 'exclude', 'include']),

    /**
     * 设置需要忽略输出监听过程的组件信息列表，仅在listenPropsMode为'exclude'时生效
     */
    excludeProps: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置需要包含输出监听过程的组件信息列表，仅在listenPropsMode为'include'时生效
     */
    includeProps: PropTypes.arrayOf(PropTypes.string),

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

MobileSkeleton.defaultProps = {
    animated: false,
    debug: false,
    listenPropsMode: 'default'
};

export default MobileSkeleton;