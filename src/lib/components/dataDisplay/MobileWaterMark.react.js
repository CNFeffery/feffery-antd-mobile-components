/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { WaterMark } from 'antd-mobile';

const MobileWaterMark = (props) => {
    let {
        id,
        key,
        style,
        className,
        content,
        fontColor,
        fontSize,
        fullPage,
        gapX,
        gapY,
        height,
        image,
        imageHeight,
        imageWidth,
        rotate,
        width,
        zIndex,
        loading_state,
        setProps
    } = props;

    return <WaterMark
        id={id}
        key={key}
        style={style}
        className={className}
        content={content}
        fontColor={fontColor}
        fontSize={fontSize}
        fullPage={fullPage}
        gapX={gapX}
        gapY={gapY}
        height={height}
        image={image}
        imageHeight={imageHeight}
        imageWidth={imageWidth}
        rotate={rotate}
        width={width}
        zIndex={zIndex}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileWaterMark.propTypes = {
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
     * 用于设置水印文字内容，当传入数组时用于表示多行文字
     */
    content: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),

    /**
     * 用于设置水印文字颜色
     * 默认：'rgba(0, 0, 0, .15)'
     */
    fontColor: PropTypes.string,

    /**
     * 用于设置水印文字大小
     * 默认：14
     */
    fontSize: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 用于设置水印是否覆盖整个页面
     * 默认：true
     */
    fullPage: PropTypes.bool,

    /**
     * 用于设置水印之间的水平像素间距
     * 默认：24
     */
    gapX: PropTypes.number,

    /**
     * 用于设置水印之间的垂直像素间距
     * 默认：48
     */
    gapY: PropTypes.number,

    /**
     * 用于设置水印像素高度
     * 默认：64
     */
    height: PropTypes.number,

    /**
     * 用于设置水印图片地址，当image与content同时设置时，优先使用图片水印
     */
    image: PropTypes.string,

    /**
     * 用于设置水印图片像素高度
     * 默认：64
     */
    imageHeight: PropTypes.number,

    /**
     * 用于设置水印图片像素宽度
     * 默认：120
     */
    imageWidth: PropTypes.number,

    /**
     * 用于设置水印图片旋转角度
     * 默认：-22
     */
    rotate: PropTypes.number,

    /**
     * 用于设置水印像素宽度
     * 默认：120
     */
    width: PropTypes.number,

    /**
     * 用于设置水印元素的z-index属性
     * 默认：2000
     */
    zIndex: PropTypes.number,

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

MobileWaterMark.defaultProps = {
    fontColor: 'rgba(0, 0, 0, .15)',
    fontSize: 14,
    fullPage: true,
    gapX: 24,
    gapY: 48,
    height: 64,
    imageHeight: 64,
    imageWidth: 120,
    rotate: -22,
    width: 120,
    zIndex: 2000,
};

export default React.memo(MobileWaterMark);