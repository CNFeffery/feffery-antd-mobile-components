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
// 辅助库
import { useLoading } from '../../utils';


/**
 * 复选框组件MobileCheckbox
 */
const MobileCheckbox = ({
    id,
    key,
    style,
    className,
    children,
    block = false,
    checked = false,
    disabled = false,
    icon,
    indeterminate = false,
    setProps
}) => {

    return <Checkbox
        id={id}
        key={key}
        style={style}
        className={className}
        block={block}
        checked={checked}
        disabled={disabled}
        icon={
            icon ?
                (_checked, _indeterminate) => {
                    if (_indeterminate) {
                        return icon.indeterminate;
                    } else if (_checked) {
                        return icon.checked;
                    }
                    return icon.unchecked;
                } :
                undefined
        }
        indeterminate={indeterminate}
        children={children}
        onChange={() => setProps({
            checked: !checked
        })}
        data-dash-is-loading={useLoading()}
    />;
};


MobileCheckbox.propTypes = {
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

    /**
     * 用于设置当前复选框标签内容
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 是否撑满父级元素
     * 默认：false
     */
    block: PropTypes.bool,

    /**
     * 设置或监听当前复选框是否选中
     * 默认：false
     */
    checked: PropTypes.bool,

    /**
     * 是否禁用当前组件
     * 默认：false
     */
    disabled: PropTypes.bool,

    /**
     * 自定义各状态下的图标元素
     */
    icon: PropTypes.exact({
        /**
         * 自定义选中状态下图标元素
         */
        checked: PropTypes.node,
        /**
         * 自定义非选中状态下图标元素
         */
        unchecked: PropTypes.node,
        /**
         * 自定义半选中状态下图标元素
         */
        indeterminate: PropTypes.node
    }),

    /**
     * 是否以半选中状态进行渲染，仅用作样式控制
     */
    indeterminate: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileCheckbox);