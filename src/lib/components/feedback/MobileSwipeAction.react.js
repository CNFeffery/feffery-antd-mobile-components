/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { SwipeAction } from 'antd-mobile';

/**
 * 滑动操作组件MobileSwipeAction
 */
const MobileSwipeAction = (props) => {
    let {
        id,
        children,
        closeOnAction,
        closeOnTouchOutside,
        leftActions,
        rightActions,
        loading_state,
        setProps
    } = props;

    return <SwipeAction
        id={id}
        leftActions={
            (leftActions || []).map(
                (item) => ({
                    ...item
                })
            )
        }
        rightActions={
            (rightActions || []).map(
                (item) => ({
                    ...item
                })
            )
        }
        closeOnAction={closeOnAction}
        closeOnTouchOutside={closeOnTouchOutside}
        onAction={(action, e) => {
            setProps({
                actionEvent: {
                    key: action.key,
                    timestamp: new Date().getTime(),
                }
            })
        }}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    >{children}</ SwipeAction>;
};

MobileSwipeAction.propTypes = {
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
     * 是否在点击操作按钮后自动归位
     * 默认值：`true`
     */
    closeOnAction: PropTypes.bool,

    /**
     * 是否在点击其他区域时自动归位
     * 默认值：`true`
     */
    closeOnTouchOutside: PropTypes.bool,

    /**
     * 配置左侧的操作按钮列表
     */
    leftActions: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 当前操作按钮唯一标识
             */
            key: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.number
            ]),
            /**
             * 当前操作按钮颜色，可设置`css`中合法的颜色值，内置的颜色有`'light'`、`'weak'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
             * 默认值：`'light'`
             */
            color: PropTypes.string,
            /**
             * 当前操作按钮内容
             */
            text: PropTypes.node
        })
    ),

    /**
     * 配置右侧的操作按钮列表
     */
    rightActions: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 当前操作按钮颜色，可设置`css`中合法的颜色值，内置的颜色有`'light'`、`'weak'`、`'primary'`、`'success'`、`'warning'`、`'danger'`
             * 默认值：`'light'`
             */
            color: PropTypes.string,
            /**
             * 当前操作按钮唯一标识
             */
            key: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.number
            ]),
            /**
             * 当前操作按钮内容
             */
            text: PropTypes.node
        })
    ),

    /**
     * 监听最近一次操作按钮点击事件
     */
    actionEvent: PropTypes.shape({
        /**
         * 操作按钮对应`key`值
         */
        key: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.number
        ]),
        /**
         * 事件对应时间戳
         */
        timestamp: PropTypes.number
    }),

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

MobileSwipeAction.defaultProps = {
    closeOnAction: true,
    closeOnTouchOutside: true
};

export default React.memo(MobileSwipeAction);