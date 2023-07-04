/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Footer } from 'antd-mobile';

const MobileFooter = (props) => {
    let {
        id,
        key,
        style,
        className,
        label,
        links,
        content,
        chips,
        loading_state,
        setProps
    } = props;

    return <Footer
        id={id}
        key={key}
        style={style}
        className={className}
        label={label}
        links={links}
        content={content}
        chips={chips}
        onChipClick={(item, _) => setProps({
            clickedChip: {
                key: item.key,
                timestamp: new Date().getTime()
            }
        })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileFooter.propTypes = {
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
     * 用于为当前页脚设置分割线内部元素
     */
    label: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.node
    ]),

    /**
     * 用于为当前页脚设置链接部分内容
     */
    links: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 用于为当前链接项设置链接文字
             */
            text: PropTypes.string,

            /**
             * 用于为当前链接项设置链接地址
             */
            href: PropTypes.string
        })
    ),

    /**
     * 用于为当前页脚设置内容区域元素
     */
    content: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.node
    ]),

    /**
     * 用于为当前页脚设置底部标签部分内容
     */
    chips: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 用于设置当前标签项的内容
             */
            text: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.node
            ]),

            /**
             * 用于设置当前标签项的类型
             * 可选的有'plain'（纯展示）、'link'（可点击）
             * 默认：'plain'
             */
            type: PropTypes.oneOf(['plain', 'link']),

            /**
             * 用于为当前标签设置唯一识别id，用于在可点击类型下监听标签点击事件
             */
            key: PropTypes.string
        })
    ),

    // 组件监听类属性
    /**
     * 用于针对可点击的标签项，监听点击事件信息
     */
    clickedChip: PropTypes.object,

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

MobileFooter.defaultProps = {
};

export default React.memo(MobileFooter);