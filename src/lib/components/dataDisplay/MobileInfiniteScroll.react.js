/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { InfiniteScroll } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 无限滚动组件MobileInfiniteScroll
 */
const MobileInfiniteScroll = ({
    id,
    threshold = 250,
    refreshCount = 0,
    stopRefreshing,
    hasMore = true,
    setProps
}) => {

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

    return <InfiniteScroll
        id={id}
        threshold={threshold}
        loadMore={
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
        hasMore={hasMore}
        data-dash-is-loading={useLoading()} />;
};

MobileInfiniteScroll.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 触发刷新对应的滚动触底像素距离阈值
     * 默认值：`250`
     */
    threshold: PropTypes.number,

    /**
     * 监听滚动到底部操作累计触发次数
     * 默认值：`0`
     */
    refreshCount: PropTypes.number,

    /**
     * 用于手动终止进行中的加载过程，每次调用会将更新为`true`后，都会在终止加载状态后，被重置为`false`
     */
    stopRefreshing: PropTypes.bool,

    /**
     * 控制是否可继续滚动触底触发新的加载
     * 默认值：`true`
     */
    hasMore: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileInfiniteScroll);