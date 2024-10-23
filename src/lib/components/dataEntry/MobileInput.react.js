/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Input } from 'antd-mobile';
// hooks
import { useRequest } from 'ahooks';

/**
 * 输入框组件MobileInput
 */
const MobileInput = (props) => {
    let {
        id,
        key,
        style,
        className,
        type,
        clearable,
        defaultValue,
        disabled,
        maxLength,
        onlyShowClearWhenFocus,
        placeholder,
        readOnly,
        value,
        debounceValue,
        debounceWait,
        loading_state,
        setProps
    } = props;

    // 解决受控value卡部分中文输入法问题
    const [rawValue, setRawValue] = useState(value);

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

    // 解决value经回调更新后，rawValue未更新的问题
    useEffect(() => {
        setRawValue(value);
    }, [value])

    return <Input
        id={id}
        key={key}
        style={style}
        className={className}
        type={type}
        clearable={clearable}
        defaultValue={defaultValue}
        disabled={disabled}
        maxLength={maxLength}
        onlyShowClearWhenFocus={onlyShowClearWhenFocus}
        placeholder={placeholder}
        readOnly={readOnly}
        value={rawValue || value}
        onChange={
            (e) => {
                setProps({
                    value: e
                })
                onDebounceChange(e)
                setRawValue(e)
            }
        }
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};


MobileInput.propTypes = {
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
     * 用于设置当前输入框的类型
     * 可选的有'text'、'password'
     * 默认：'text'
     */
    type: PropTypes.oneOf(['text', 'password']),

    /**
     * 是否渲染清除按钮
     * 默认：false
     */
    clearable: PropTypes.bool,

    /**
     * 设置初始化已输入内容
     */
    defaultValue: PropTypes.string,

    /**
     * 是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 限制允许输入内容的长度上限
     * 默认无限制
     */
    maxLength: PropTypes.number,

    /**
     * 是否仅在当前输入框聚焦时才显示取消按钮
     * 默认：true
     */
    onlyShowClearWhenFocus: PropTypes.bool,

    /**
     * 提示文本内容
     */
    placeholder: PropTypes.string,

    /**
     * 用于设置是否以只读模式渲染当前组件
     * 默认：false
     */
    readOnly: PropTypes.bool,

    /**
     * 设置或监听当前输入框内的已输入文字内容
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

MobileInput.defaultProps = {
    type: 'text',
    clearable: false,
    disabled: false,
    onlyShowClearWhenFocus: true,
    readOnly: false,
    debounceWait: 200
};

export default React.memo(MobileInput);