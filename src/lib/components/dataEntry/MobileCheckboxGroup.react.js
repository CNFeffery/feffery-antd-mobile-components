/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Checkbox } from 'antd-mobile';
// 工具函数
import { isUndefined } from 'lodash';

/**
 * 复选框组合组件MobileCheckboxGroup
 */
const MobileCheckboxGroup = (props) => {
    let {
        id,
        key,
        style,
        className,
        options,
        block,
        defaultValue,
        disabled,
        value,
        loading_state,
        setProps
    } = props;

    // 处理defaultValue、value的初始化逻辑
    useEffect(() => {
        if (isUndefined(value) && defaultValue) {
            setProps({
                value: defaultValue
            })
        }
    }, [])

    return <Checkbox.Group
        id={id}
        key={key}
        style={style}
        className={className}
        defaultValue={defaultValue}
        disabled={disabled}
        value={value}
        children={
            options.map(
                (option) => <Checkbox style={option.style}
                    className={option.className}
                    disabled={option.disabled}
                    value={option.value}
                    children={option.label}
                    block={block} />
            )
        }
        onChange={(e) => setProps({ value: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};


MobileCheckboxGroup.propTypes = {
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
     * 用于为当前复选框组定义选项
     */
    options: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 是否禁用当前项
             * 默认：false
             */
            disabled: PropTypes.bool,

            /**
             * 当前项标签内容
             */
            label: PropTypes.node,

            /**
             * 当前项对应值
             */
            value: PropTypes.string,

            /**
             * 当前项css样式
             */
            style: PropTypes.object,

            /**
             * 当前项css类名
             */
            className: PropTypes.string
        })
    ),

    /**
     * 每个选项是否独占一行
     * 默认：true
     */
    block: PropTypes.bool,

    /**
     * 设置初始化时选中值对应数组
     * 默认：[]
     */
    defaultValue: PropTypes.arrayOf(PropTypes.string),

    /**
     * 是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 设置或监听已选中值对应数组
     */
    value: PropTypes.arrayOf(PropTypes.string),

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

MobileCheckboxGroup.defaultProps = {
    options: [],
    block: true,
    defaultValue: [],
    disabled: false
};

export default React.memo(MobileCheckboxGroup);