/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Image } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 图片组件MobileImage
 */
const MobileImage = ({
    id,
    key,
    style,
    className,
    alt,
    draggable = false,
    fallback,
    fit = 'fill',
    height,
    lazy = false,
    src,
    width,
    nClicks = 0,
    setProps
}) => {

    return <Image
        id={id}
        key={key}
        style={style}
        className={className}
        alt={alt}
        draggable={draggable}
        fallback={fallback}
        fit={fit}
        height={height}
        lazy={lazy}
        src={src}
        width={width}
        onClick={() => setProps({ nClicks: nClicks + 1 })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileImage.propTypes = {
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
     * 用于设置当前图片的描述文字
     */
    alt: PropTypes.string,

    /**
     * 用于设置当前图片是否可拖拽
     * 默认：false
     */
    draggable: PropTypes.bool,

    // 组件常规参数
    /**
     * 用于为当前图片组件设置加载失败时的占位图
     */
    fallback: PropTypes.node,

    /**
     * 用于设置当前图片的填充模式
     * 可选的有'contain'、'cover'、'fill'、'none'、'scale-down'
     * 默认：'fill'
     */
    fit: PropTypes.oneOf(['contain', 'cover', 'fill', 'none', 'scale-down']),

    /**
     * 用于设置当前图片的高度
     * 当传入数值型时会被视作像素高度
     */
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

    /**
     * 用于设置当前图片是否开启懒加载功能
     * 默认：false
     */
    lazy: PropTypes.bool,

    /**
     * 用于设置当前图片资源地址
     */
    src: PropTypes.string,

    /**
     * 用于设置当前图片的宽度
     * 当传入数值型时会被视作像素宽度
     */
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

    // 组件监听类属性
    /**
     * 用于记录当前图片累计被点击次数
     */
    nClicks: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileImage);