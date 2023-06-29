/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Ellipsis } from 'antd-mobile';

const MobileEllipsis = (props) => {
    let {
        id,
        key,
        style,
        className,
        collapseText,
        content,
        direction,
        expandText,
        rows,
        defaultExpanded,
        loading_state,
        setProps
    } = props;

    return <Ellipsis
        id={id}
        key={key}
        style={style}
        className={className}
        collapseText={collapseText}
        content={content}
        direction={direction}
        expandText={expandText}
        rows={rows}
        defaultExpanded={defaultExpanded}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileEllipsis.propTypes = {
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
     * 用于设置收起操作文案内容
     * 默认：''
     */
    collapseText: PropTypes.node,

    /**
     * 用于设置文字内容
     */
    content: PropTypes.string,

    /**
     * 用于设置省略位置，可选的有'start'、'end'、'middle'
     * 默认：'end'
     */
    direction: PropTypes.oneOf(['start', 'end', 'middle']),

    /**
     * 用于设置展开操作文案内容
     */
    expandText: PropTypes.node,

    /**
     * 用于设置展示文字内容的行数
     * 默认：1
     */
    rows: PropTypes.number,

    /**
     * 用于设置初始化时候展开
     * 默认：false
     */
    defaultExpanded: PropTypes.bool,

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

MobileEllipsis.defaultProps = {
    collapseText: '',
    direction: 'end',
    rows: 1,
    defaultExpanded: false
};

export default React.memo(MobileEllipsis);