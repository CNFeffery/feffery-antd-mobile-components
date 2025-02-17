/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Stepper } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 步进器组件MobileStepper
 */
const MobileStepper = ({
    id,
    key,
    style,
    className,
    allowEmpty = false,
    defaultValue = 0,
    value,
    digits,
    disabled = false,
    inputReadOnly = false,
    max,
    min,
    step = 1,
    stringMode = false,
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

    return <Stepper
        id={id}
        key={key}
        style={style}
        className={className}
        allowEmpty={allowEmpty}
        defaultValue={defaultValue}
        value={value}
        digits={digits}
        disabled={disabled}
        inputReadOnly={inputReadOnly}
        max={max}
        min={min}
        step={step}
        stringMode={stringMode}
        onChange={(e) => setProps({ value: e })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileStepper.propTypes = {
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
     * 是否允许输入内容为空
     * 默认值：`false`
     */
    allowEmpty: PropTypes.bool,

    /**
     * 设置默认输入值
     * 默认值：`0`
     */
    defaultValue: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 监听或设置输入值
     */
    value: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 格式化对应小数点后固定位数
     */
    digits: PropTypes.number,

    /**
     * 是否禁用当前步进器
     * 默认值：`false`
     */
    disabled: PropTypes.bool,

    /**
     * 输入框是否只读
     * 默认值：`false`
     */
    inputReadOnly: PropTypes.bool,

    /**
     * 限定最大值
     */
    max: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限定最小值
     */
    min: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 步进对应数值步长
     * 默认值：`1`
     */
    step: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 是否开启高精度字符值模式，开启后`defaultValue`、`value`、`min`、`max`等参数为字符型
     * 默认值：`false`
     */
    stringMode: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileStepper);