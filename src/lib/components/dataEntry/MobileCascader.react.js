/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Cascader } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 级联选择组件MobileCascader
 */
const MobileCascader = ({
    id,
    key,
    style,
    className,
    cancelText = '取消',
    confirmText = '确认',
    defaultValue,
    destroyOnClose = true,
    forceRender = false,
    options = [],
    placeholder = '请选择',
    title,
    value,
    visible = false,
    setProps
}) => {

    // 处理defaultValue、value的初始化逻辑
    useEffect(() => {
        if (defaultValue && !value) {
            setProps({
                value: defaultValue
            })
        }
    }, [])

    return <Cascader
        id={id}
        key={key}
        style={style}
        className={className}
        cancelText={cancelText}
        confirmText={confirmText}
        defaultValue={defaultValue}
        destroyOnClose={destroyOnClose}
        forceRender={forceRender}
        options={options}
        placeholder={placeholder}
        title={title}
        value={value}
        visible={visible}
        onConfirm={(e) => setProps({ value: e })}
        onClose={() => setProps({ visible: !visible })}
        data-dash-is-loading={useLoading()}
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


MobileCascader.propTypes = {
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
     * 用于为当前级联选择设置取消按钮文案信息
     * 默认：'取消'
     */
    cancelText: PropTypes.string,

    /**
     * 用于为当前级联选择设置确认按钮文案信息
     * 默认：'确认'
     */
    confirmText: PropTypes.string,

    /**
     * 用于为当前级联选择设置默认选中项
     */
    defaultValue: PropTypes.arrayOf(
        PropTypes.string
    ),

    /**
     * 当前级联选择组件不可见时是否进行销毁
     * 默认：true
     */
    destroyOnClose: PropTypes.bool,

    /**
     * 用于设置初始化时是否强制渲染当前级联选择组件
     * 默认：false
     */
    forceRender: PropTypes.bool,

    /**
     * 用于为当前级联选择组件配置级联选项数据
     * 默认：[]
     */
    options: optionsPropTypes,

    /**
     * 用于为当前级联选择设置无选中项时的提示文字
     * 默认：'请选择'
     */
    placeholder: PropTypes.string,

    /**
     * 为当前级联选择设置标题内容
     */
    title: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.node
    ]),

    /**
     * 用于设置或监听当前已选中项
     */
    value: PropTypes.arrayOf(
        PropTypes.string
    ),

    /**
     * 用于设置是否显示当前级联选择
     * 默认：false
     */
    visible: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileCascader);