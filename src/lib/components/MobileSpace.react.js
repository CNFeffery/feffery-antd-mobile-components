/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Space } from 'antd-mobile';

const MobileSpace = (props) => {
    let {
        id,
        key,
        style,
        className,
        children,
        align,
        block,
        direction,
        justify,
        wrap,
        nClicks,
        loading_state,
        setProps
    } = props;

    return <Space
        id={id}
        key={key}
        style={style}
        className={className}
        children={children}
        align={align}
        block={block}
        direction={direction}
        justify={justify}
        wrap={wrap}
        onClick={() => setProps({ nClicks: nClicks + 1 })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileSpace.propTypes = {
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
     * 用于设置内部元素
     */
    children: PropTypes.node,

    // 组件常规参数
    /**
     * 用于设置当前间距组件的交叉轴对齐方式
     * 可选的有'start'、'end'、'center'、'baseline'
     */
    align: PropTypes.oneOf(['start', 'end', 'center', 'baseline']),

    /**
     * 用于设置当前间距组件是否撑满父元素
     * 默认：false
     */
    block: PropTypes.bool,

    /**
     * 用于设置当前间距组件的方向
     * 可选的有'vertical'、'horizontal'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 用于设置当前间距组件的主轴对齐方式
     * 可选的有'start'、'end'、'center'、'between'、'around'、'evenly'、'stretch'
     */
    justify: PropTypes.oneOf(['start', 'end', 'center', 'between', 'around', 'evenly', 'stretch']),

    /**
     * 用于设置当前间距组件是否自动换行，仅在'horizontal'方向下有效
     * 默认：false
     */
    wrap: PropTypes.bool,

    // 组件监听类属性
    /**
     * 用于记录当前间距组件累计被点击次数
     */
    nClicks: PropTypes.number,

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

MobileSpace.defaultProps = {
    block: false,
    direction: 'horizontal',
    wrap: false,
    nClicks: 0
};

export default React.memo(MobileSpace);