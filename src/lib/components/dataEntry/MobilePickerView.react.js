/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { PickerView } from 'antd-mobile';

/**
 * 选择器视图组件MobilePickerView
 */
const MobilePickerView = (props) => {
    let {
        id,
        key,
        style,
        className,
        columns,
        defaultValue,
        value,
        mouseWheel,
        loading,
        loadingContent,
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

    return <PickerView
        id={id}
        key={key}
        style={style}
        className={className}
        columns={columns}
        defaultValue={defaultValue}
        value={value}
        mouseWheel={mouseWheel}
        loading={loading}
        loadingContent={loadingContent}
        onChange={(e) => setProps({ value: e })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobilePickerView.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 配置各列选项
     */
    columns: PropTypes.arrayOf(
        PropTypes.arrayOf(
            PropTypes.exact({
                /**
                 * 当前选项标题
                 */
                label: PropTypes.string,
                /**
                 * 当前选项值
                 */
                value: PropTypes.string
            })
        )
    ),

    /**
     * 设置默认选中值
     * 默认值：`[]`
     */
    defaultValue: PropTypes.arrayOf(PropTypes.string),

    /**
     * 监听或设置当前选中值
     */
    value: PropTypes.arrayOf(PropTypes.string),

    /**
     * 是否启用鼠标滚轮辅助选择
     * 默认值：`false`
     */
    mouseWheel: PropTypes.bool,

    /**
     * 设置是否渲染为“加载中”状态
     * 默认值：`false`
     */
    loading: PropTypes.bool,

    /**
     * 组件型，“加载中”状态下展示的内容
     */
    loadingContent: PropTypes.node,

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

MobilePickerView.defaultProps = {
    defaultValue: [],
    mouseWheel: false,
    loading: false
};

export default React.memo(MobilePickerView);