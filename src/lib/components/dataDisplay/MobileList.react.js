/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { List } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 列表组件MobileList
 */
const MobileList = ({
    id,
    key,
    style,
    className,
    items = [],
    title,
    mode = 'default',
    setProps
}) => {

    return <List
        id={id}
        key={key}
        style={style}
        className={className}
        title={title}
        mode={mode}
        children={
            items.map(
                (item) => <List.Item
                    onClick={
                        item.clickable ?
                            () => {
                                setProps({
                                    clickedItem: {
                                        key: item.key,
                                        timestamp: new Date().getTime()
                                    }
                                })
                            } :
                            undefined
                    }
                    {...item} />
            )
        }
        data-dash-is-loading={useLoading()}
    />;
};

MobileList.propTypes = {
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
     * 用于定义内部各子项
     */
    items: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 必填，用于设置当前子项的唯一识别id
             */
            key: PropTypes.string.isRequired,

            /**
             * 用于设置当前子项右侧是否显示箭头图标
             * 也可传入组件型输入充当自定义图标
             * 默认：与clickable一致
             */
            arrow: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.node
            ]),

            /**
             * 用于设置当前子项中间区域的主内容
             */
            children: PropTypes.node,

            /**
             * 用于设置当前子项是否展示可点击效果
             * 默认：false
             */
            clickable: PropTypes.bool,

            /**
             * 用于设置当前子项中间下部的描述区域内容
             */
            description: PropTypes.node,

            /**
             * 用于设置是否禁用当前子项
             * 默认：false
             */
            disabled: PropTypes.bool,

            /**
             * 用于设置当前子项右侧区域内容
             */
            extra: PropTypes.node,

            /**
             * 用于设置当前子项左侧区域内容
             */
            prefix: PropTypes.node,

            /**
             * 用于设置当前子项中间上部的标题区域内容
             */
            title: PropTypes.node
        })
    ),

    /**
     * 用于设置当前列表标题内容
     */
    title: PropTypes.node,

    /**
     * 用于设置当前列表的渲染方式
     * 可选的有'default'、'card'
     * 默认：'default'
     */
    mode: PropTypes.oneOf(['default', 'card']),

    // 组件监听类属性
    /**
     * 用于针对可点击的子项，监听点击事件信息
     */
    clickedItem: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileList);