/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Tabs } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 标签页组件MobileTabs
 */
const MobileTabs = ({
    id,
    key,
    style,
    className,
    items = [],
    activeKey,
    activeLineMode = 'auto',
    defaultActiveKey,
    stretch = true,
    setProps
}) => {

    return <Tabs
        id={id}
        key={key}
        style={style}
        className={className}
        children={
            items.map(
                (item) => {
                    return (<Tabs.Tab {...item} />);
                }
            )
        }
        activeKey={activeKey}
        activeLineMode={activeLineMode}
        defaultActiveKey={defaultActiveKey}
        stretch={stretch}
        onChange={(e) => setProps({ activeKey: e })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileTabs.propTypes = {
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
             * 可选，用于设置当前选项对应的内容
             */
            children: PropTypes.node,

            /**
             * 用于设置是否禁用当前选项
             * 默认：false
             */
            disabled: PropTypes.bool,

            /**
             * 用于设置初始化时，若当前选项不可见，是否对其对应的children内容进行渲染
             * 默认：false
             */
            forceRender: PropTypes.bool,

            /**
             * 用于设置当前选项被隐藏后，是否对其children内容进行销毁
             * 默认：false
             */
            destroyOnClose: PropTypes.bool
        })
    ),

    /**
     * 用于设置或监听当前被激活的选项对应key值
     */
    activeKey: PropTypes.string,

    /**
     * 用于设置已激活选项下划线模式
     * 可选的有'auto'、'full'、'fixed'
     * 默认：'auto'
     */
    activeLineMode: PropTypes.oneOf(['auto', 'full', 'fixed']),

    /**
     * 用于设置初始化时，处于被激活状态的选项对应key值
     * 默认激活items中按顺序第一位的选项
     */
    defaultActiveKey: PropTypes.string,

    /**
     * 用于设置选项卡头部是否拉伸
     * 默认：true
     */
    stretch: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileTabs);