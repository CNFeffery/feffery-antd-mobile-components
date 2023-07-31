/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { CheckList } from 'antd-mobile';

const MobileCheckList = (props) => {
    let {
        id,
        key,
        style,
        className,
        options,
        defaultValue,
        disabled,
        multiple,
        readOnly,
        value,
        loading_state,
        setProps
    } = props;

    // 处理defaultValue、value的初始化逻辑
    useEffect(() => {
        if (defaultValue && !value) {
            setProps({
                value: defaultValue
            })
        }
    }, [])

    return <CheckList
        id={id}
        key={key}
        style={style}
        className={className}
        defaultValue={defaultValue}
        disabled={disabled}
        multiple={multiple}
        readOnly={readOnly}
        value={value}
        children={
            options.map(
                (option) => <CheckList.Item {...option} />
            )
        }
        onChange={(e) => setProps({ value: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};


MobileCheckList.propTypes = {
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
     * 用于为当前可勾选列表定义选项
     */
    options: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 用于设置当前选项主要区域元素
             */
            children: PropTypes.node,

            /**
             * 用于设置当前选项的值
             */
            value: PropTypes.string,

            /**
             * 用于设置当前选项中间上部的标题区域元素
             */
            title: PropTypes.node,

            /**
             * 用于设置当前选项中间下部的描述区域元素
             */
            description: PropTypes.node,

            /**
             * 用于设置当前选项左侧区域元素
             */
            prefix: PropTypes.node,

            /**
             * 用于设置是否禁用当前选项
             * 默认：false
             */
            disabled: PropTypes.bool,

            /**
             * 用于设置是否以只读模式渲染当前选项
             * 默认：false
             */
            readOnly: PropTypes.bool
        })
    ),

    /**
     * 用于设置当前可勾选列表组件的默认选中项
     */
    defaultValue: PropTypes.arrayOf(PropTypes.string),

    /**
     * 用于设置是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 用于设置是否允许多选
     * 默认：false
     */
    multiple: PropTypes.bool,

    /**
     * 用于设置是否以只读模式渲染当前组件
     * 默认：false
     */
    readOnly: PropTypes.bool,

    /**
     * 用于设置或监听当前可勾选列表组件的选中项
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

MobileCheckList.defaultProps = {
    options: [],
    disabled: false,
    multiple: false,
    readOnly: false,
};

export default React.memo(MobileCheckList);