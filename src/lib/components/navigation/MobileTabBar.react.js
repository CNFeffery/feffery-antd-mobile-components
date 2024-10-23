/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { TabBar, Badge } from 'antd-mobile';

/**
 * 标签栏组件MobileTabBar
 */
const MobileTabBar = (props) => {
    let {
        id,
        key,
        style,
        className,
        items,
        activeKey,
        defaultActiveKey,
        safeArea,
        loading_state,
        setProps
    } = props;

    // 初始化同步props
    useEffect(() => {
        if (defaultActiveKey && !activeKey) {
            setProps({
                activeKey: defaultActiveKey
            })
        }
    }, [])

    return <TabBar
        id={id}
        key={key}
        style={style}
        className={className}
        children={
            items.map(
                (item) => {
                    return (<TabBar.Item
                        {
                        ...{
                            ...item,
                            badge: item.badge === 'dot' ? Badge.dot : item.badge
                        }
                        } />);
                }
            )
        }
        activeKey={activeKey}
        defaultActiveKey={defaultActiveKey}
        safeArea={safeArea}
        onChange={(e) => setProps({ activeKey: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileTabBar.propTypes = {
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
     * 用于定义内部各选项相关信息
     */
    items: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 必填，用于设置当前选项对应的唯一标识值
             */
            key: PropTypes.string.isRequired,

            /**
             * 必填，用于设置当前选项对应的标题内容
             */
            title: PropTypes.node.isRequired,

            /**
             * 用于设置当前选项对应的额外图标
             */
            icon: PropTypes.node,

            /**
             * 用于为当前选项设置额外的徽标信息
             * 特别地，当传入'dot'时会渲染小红点徽标
             */
            badge: PropTypes.node
        })
    ),

    /**
     * 用于设置或监听当前被激活的选项对应key值
     */
    activeKey: PropTypes.string,

    /**
     * 用于设置初始化时，处于被激活状态的选项对应key值
     * 默认激活items中按顺序第一位的选项
     */
    defaultActiveKey: PropTypes.string,

    /**
     * 用于设置是否开启安全区适配功能
     * 默认：false
     */
    safeArea: PropTypes.bool,

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

MobileTabBar.defaultProps = {
    items: [],
    safeArea: false
};

export default React.memo(MobileTabBar);