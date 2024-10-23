/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Grid } from 'antd-mobile';

/**
 * 栅格组件MobileGrid
 */
const MobileGrid = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        columns,
        gap,
        loading_state,
        setProps
    } = props;

    return <Grid
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        columns={columns}
        gap={gap}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileGrid.propTypes = {
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
     * 用于设置内部元素，通常应为若干MobileGridItem组成的列表
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 用于设置当前栅格组件的列数
     */
    columns: PropTypes.number,

    /**
     * 用于设置当前栅格组件各栅格项之间的间距
     * 也可传入格式如[水平间距, 竖直间距]的数组
     * 默认：0
     */
    gap: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string,
        PropTypes.arrayOf(
            PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.number
            ])
        )
    ]),

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

MobileGrid.defaultProps = {
    gap: 0
};

export default React.memo(MobileGrid);