/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { PullToRefresh } from 'antd-mobile';
import { sleep } from 'antd-mobile/es/utils/sleep'

/**
 * 下拉刷新组件MobilePullToRefresh
 */
const MobilePullToRefresh = (props) => {
    let {
        id,
        children,
        canReleaseText,
        completeDelay,
        completeText,
        disabled,
        headHeight,
        pullingText,
        refreshingText,
        threshold,
        refreshCount,
        stopRefreshing,
        loading_state,
        setProps
    } = props;

    // 加载执行中标识
    const _refreshing = useRef(false);

    // 每次stopRefreshing更新后，尝试终止进行中的加载状态
    useEffect(() => {
        if (stopRefreshing) {
            if (_refreshing.current) {
                _refreshing.current = false;
            }
            // 重置stopRefreshing
            setProps({
                stopRefreshing: false
            })
        }
    }, [stopRefreshing])

    return <PullToRefresh
        id={id}
        canReleaseText={canReleaseText}
        completeDelay={completeDelay}
        completeText={completeText}
        disabled={disabled}
        headHeight={headHeight}
        pullingText={pullingText}
        refreshingText={refreshingText}
        threshold={threshold}
        onRefresh={
            () => {
                // 更新refreshCount计数
                setProps({
                    refreshCount: refreshCount + 1
                })
                return new Promise(
                    (resolve) => {
                        // 更新加载执行中标识
                        _refreshing.current = true;
                        // 轮询检测是否加载完成
                        const timer = setInterval(
                            () => {
                                if (!_refreshing.current) {
                                    clearInterval(timer);
                                    resolve();
                                }
                            },
                            200
                        );
                    }
                )
            }
        }
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    >{children}</ PullToRefresh>;
};

MobilePullToRefresh.propTypes = {
    /**
     * 用于设置当前组件唯一id
     */
    id: PropTypes.string,

    /**
     * 强制重绘当前组件时使用
     */
    key: PropTypes.string,

    /**
     * 用于设置触发目标元素
     */
    children: PropTypes.node,

    /**
     * 组件型，设置释放的提示文案
     */
    canReleaseText: PropTypes.node,

    /**
     * 每次下拉刷新操作后，延迟消失时长，单位：毫秒
     * 默认值：`500`
     */
    completeDelay: PropTypes.number,

    /**
     * 组件型，设置完成时的提示文案
     */
    completeText: PropTypes.node,

    /**
     * 是否禁用下拉刷新功能
     * 默认值：`false`
     */
    disabled: PropTypes.bool,

    /**
     * 头部提示内容区像素高度
     * 默认值：`40`
     */
    headHeight: PropTypes.number,

    /**
     * 组件型，设置下拉的提示文案
     */
    pullingText: PropTypes.node,

    /**
     * 组件型，刷新时的提示文案
     */
    refreshingText: PropTypes.node,

    /**
     * 触发刷新对应的最小下拉像素距离
     * 默认值：`60`
     */
    threshold: PropTypes.number,

    /**
     * 监听下拉刷新操作累计触发次数
     * 默认值：`0`
     */
    refreshCount: PropTypes.number,

    /**
     * 用于手动终止进行中的加载过程，每次调用会将更新为`true`后，都会在终止加载状态后，被重置为`false`
     */
    stopRefreshing: PropTypes.bool,

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

MobilePullToRefresh.defaultProps = {
    completeDelay: 500,
    disabled: false,
    headHeight: 40,
    threshold: 60,
    refreshCount: 0
};

export default React.memo(MobilePullToRefresh);