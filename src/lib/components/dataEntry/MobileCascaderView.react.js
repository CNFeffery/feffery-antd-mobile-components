/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { CascaderView } from 'antd-mobile';

/**
 * 级联选择视图组件MobileCascaderView
 */
const MobileCascaderView = (props) => {
    let {
        id,
        key,
        style,
        className,
        defaultValue,
        options,
        placeholder,
        value,
        loading,
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

    return <CascaderView
        id={id}
        key={key}
        style={style}
        className={className}
        defaultValue={defaultValue}
        options={options}
        placeholder={placeholder}
        value={value}
        loading={loading}
        onChange={(e) => setProps({ value: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

// 定义选项options参数的类型约束
const optionNodeShape = {
    /**
     * 用于设置当前选项的标题内容
     */
    label: PropTypes.string,

    /**
     * 用于设置当前选项对应值
     */
    value: PropTypes.string,

    /**
     * 用于设置是否禁用当前选项
     * 默认：false
     */
    disabled: PropTypes.bool
}

const optionNodePropType = PropTypes.exact(optionNodeShape)
optionNodeShape.children = PropTypes.arrayOf(optionNodePropType)
const optionsPropTypes = PropTypes.arrayOf(optionNodePropType)


MobileCascaderView.propTypes = {
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
     * 用于为当前级联选择视图设置默认选中项
     */
    defaultValue: PropTypes.arrayOf(
        PropTypes.string
    ),

    /**
     * 用于为当前级联选择视图组件配置级联选项数据
     * 默认：[]
     */
    options: optionsPropTypes,

    /**
     * 用于为当前级联选择视图设置无选中项时的提示文字
     * 默认：'请选择'
     */
    placeholder: PropTypes.string,

    /**
     * 用于设置或监听当前已选中项
     */
    value: PropTypes.arrayOf(
        PropTypes.string
    ),

    /**
     * 用于为当前级联选择视图组件设置是否开启加载中状态
     * 默认：false
     */
    loading: PropTypes.bool,

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

MobileCascaderView.defaultProps = {
    options: [],
    placeholder: '请选择',
    loading: false
};

export default React.memo(MobileCascaderView);