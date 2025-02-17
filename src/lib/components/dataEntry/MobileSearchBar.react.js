/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { SearchBar } from 'antd-mobile';
// 辅助库
import { useRequest } from 'ahooks';
import { useLoading } from '../../utils';


/**
 * 搜索框组件MobileSearchBar
 */
const MobileSearchBar = ({
    id,
    key,
    style,
    className,
    cancelText = '取消',
    clearOnCancel = true,
    clearable = true,
    icon,
    maxLength,
    onlyShowClearWhenFocus = false,
    placeholder,
    showCancelButton = false,
    value,
    debounceWait = 200,
    setProps
}) => {

    // 针对debounceValue的防抖监听更新
    const { run: onDebounceChange } = useRequest(
        (e) => {
            setProps({
                debounceValue: e
            })
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    return <SearchBar
        id={id}
        key={key}
        style={style}
        className={className}
        cancelText={cancelText}
        clearOnCancel={clearOnCancel}
        clearable={clearable}
        icon={icon}
        maxLength={maxLength}
        onlyShowClearWhenFocus={onlyShowClearWhenFocus}
        placeholder={placeholder}
        showCancelButton={showCancelButton}
        value={value}
        onChange={
            (e) => {
                setProps({
                    value: e
                })
                onDebounceChange(e)
            }
        }
        data-dash-is-loading={useLoading()}
    />;
};


MobileSearchBar.propTypes = {
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
     * 取消按钮文案
     * 默认：'取消'
     */
    cancelText: PropTypes.string,

    /**
     * 点击取消按钮后是否清空已输入内容
     * 默认：true
     */
    clearOnCancel: PropTypes.bool,

    /**
     * 是否渲染取消按钮
     * 默认：true
     */
    clearable: PropTypes.bool,

    /**
     * 自定义前缀图标
     */
    icon: PropTypes.node,

    /**
     * 限制允许输入内容的长度上限
     * 默认无限制
     */
    maxLength: PropTypes.number,

    /**
     * 是否仅在当前搜索框聚焦时才显示取消按钮
     * 默认：false
     */
    onlyShowClearWhenFocus: PropTypes.bool,

    /**
     * 提示文本内容
     */
    placeholder: PropTypes.string,

    /**
     * 是否在搜索框右侧显示取消按钮
     * 默认：false
     */
    showCancelButton: PropTypes.bool,

    /**
     * 设置或监听当前搜索框内的已输入文字内容
     */
    value: PropTypes.string,

    /**
     * value的防抖状态值
     */
    debounceValue: PropTypes.string,

    /**
     * 针对debounceValue的防抖延时，单位：毫秒
     * 默认：200
     */
    debounceWait: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileSearchBar);