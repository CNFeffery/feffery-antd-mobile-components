/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';

/**
 * 手机设备模拟组件MobileMockPhone
 */
const MobileMockPhone = (props) => {
    let {
        id,
        children,
        width,
        height,
        loading_state,
        setProps
    } = props;

    return (
        <div id={id}
            style={{
                width: width || 433,
                height: height || 882,
                border: '16px solid #19191d',
                borderRadius: 60,
                boxSizing: 'border-box',
                position: 'relative'
            }}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {/* 灵动岛 */}
            <div style={{
                position: 'absolute',
                width: '25%',
                height: 28,
                background: '#020202',
                borderRadius: 16,
                top: 8,
                left: '50%',
                transform: 'translateX(-50%)'
            }} />
            {/* 前置摄像头 */}
            <div style={{
                position: 'absolute',
                width: 10,
                height: 10,
                borderRadius: '50%',
                background: '#0d0e1e',
                top: 17,
                left: '50%',
                transform: 'translateX(-50%)'
            }} />
            {/* 底部操作条 */}
            <div style={{
                position: 'absolute',
                width: '36%',
                height: 6,
                bottom: 8,
                left: '50%',
                transform: 'translateX(-50%)',
                background: '#282828',
                borderRadius: 10,
            }} />
            {/* 内容容器 */}
            <div style={{
                position: 'absolute',
                top: 42,
                left: 0,
                right: 0,
                bottom: 0,
                overflow: 'auto',
                scrollbarWidth: 'none',
                padding: '0 0 40px 0'
            }}>
                {children}
            </div>
        </div>
    );
};

MobileMockPhone.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 用于设置内部元素
     */
    children: PropTypes.node,

    /**
     * 窗口像素宽度
     * 默认值：`433`
     */
    width: PropTypes.number,

    /**
     * 窗口像素高度
     * 默认值：`882`
     */
    height: PropTypes.number,

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

MobileMockPhone.defaultProps = {
    width: 433,
    height: 882
};

export default React.memo(MobileMockPhone);