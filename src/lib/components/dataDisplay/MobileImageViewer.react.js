/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { ImageViewer } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 图片查看器组件MobileImageViewer
 */
const MobileImageViewer = ({
    id,
    key,
    style,
    className,
    mode = 'default',
    defaultIndex = 0,
    image,
    images,
    maxZoom = 3,
    visible = false,
    setProps
}) => {

    if (mode === 'default') {
        return <ImageViewer
            id={id}
            key={key}
            style={style}
            className={className}
            image={image}
            maxZoom={maxZoom}
            visible={visible}
            onClose={() => setProps({ visible: false })}
            data-dash-is-loading={useLoading()}
        />;
    }
    return <ImageViewer.Multi
        id={id}
        key={key}
        style={style}
        className={className}
        defaultIndex={defaultIndex}
        images={images}
        maxZoom={maxZoom}
        visible={visible}
        onClose={() => setProps({ visible: false })}
        data-dash-is-loading={useLoading()}
    />;
};

MobileImageViewer.propTypes = {
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
     * 用于设置当前图片查看器的显示模式
     * 可选的有'default'、'multiple'，分别对应参数image、images
     * 默认：'default'
     */
    mode: PropTypes.oneOf(['default', 'multiple']),

    /**
     * 当mode='multiple'时，用于设置默认显示的图片位序
     * 默认：0
     */
    defaultIndex: PropTypes.number,

    /**
     * 当mode='default'时，用于设置目标图片资源地址
     */
    image: PropTypes.string,

    /**
     * 当mode='multiple'时，用于设置目标图片资源地址数组
     */
    images: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置图片查看时的最大缩放倍数
     * 默认：3
     */
    maxZoom: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.oneOf(['auto'])
    ]),

    /**
     * 用于监听或设置当前图片查看器是否处于显示状态
     * 默认：false
     */
    visible: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileImageViewer);