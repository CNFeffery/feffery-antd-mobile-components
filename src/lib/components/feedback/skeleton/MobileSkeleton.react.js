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
// 辅助库
import { equals } from 'ramda';
import { useLoading, loadingSelector } from '../../../utils';

/**
 * 骨架屏组件MobileSkeleton
 */
const MobileSkeleton = ({
    id,
    key,
    style,
    className,
    children,
    animated = false,
    debug = false,
    listenPropsMode = 'default',
    excludeProps,
    includeProps,
    setProps
}) => {

    const ctx = window.dash_component_api.useDashContext();
    // 获取内部加载中组件信息
    const loading_info = ctx.useSelector(loadingSelector(ctx.componentPath), equals);

    const [showLoading, setShowLoading] = useState(false);
    const timer = useRef();

    useEffect(() => {
        if (loading_info) {
            if (timer.current) {
                clearTimeout(timer.current);
            }
            if (loading_info.length > 0 && !showLoading) {
                // 当listenPropsMode为'default'时
                if (listenPropsMode === 'default') {
                    if (debug) {
                        loading_info.forEach(item => console.log(item.id + '.' + item.property))
                    }
                    setShowLoading(true);
                } else if (listenPropsMode === 'exclude') {
                    // 当listenPropsMode为'exclude'模式时
                    // 当前触发加载状态的组件+属性组合均不在排除列表中时，激活动画
                    if (loading_info.every(item => excludeProps.indexOf(item.id + '.' + item.property) === -1)) {
                        if (debug) {
                            loading_info.forEach(item => console.log(item.id + '.' + item.property))
                        }
                        setShowLoading(true);
                    }
                } else if (listenPropsMode === 'include') {
                    // 当listenPropsMode为'include'模式时
                    // 当前触发加载状态的组件+属性组合至少有一个在包含列表中时，激活动画
                    if (loading_info.some(item => includeProps.indexOf(item.id + '.' + item.property) !== -1)) {
                        if (debug) {
                            loading_info.forEach(item => console.log(item.id + '.' + item.property))
                        }
                        setShowLoading(true);
                    }
                }

            } else if (loading_info.length === 0 && showLoading) {
                timer.current = setTimeout(() => setShowLoading(false));
            }
        }
    }, [loading_info]);

    const component_loading = useLoading();

    return (
        showLoading ?
            <Skeleton
                id={id}
                key={key}
                style={style}
                className={className}
                animated={animated}
                data-dash-is-loading={component_loading}
            /> :
            <>{children}</>
    )
};

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

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default MobileSkeleton;