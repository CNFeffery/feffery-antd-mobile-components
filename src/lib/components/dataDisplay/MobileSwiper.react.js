/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Swiper } from 'antd-mobile';

const MobileSwiper = (props) => {
    let {
        id,
        key,
        style,
        className,
        items,
        allowTouchMove,
        autoplay,
        autoplayInterval,
        defaultIndex,
        direction,
        loop,
        rubberband,
        slideSize,
        stuckAtBoundary,
        trackOffset,
        loading_state,
        setProps
    } = props;

    return <Swiper
        id={id}
        key={key}
        style={style}
        className={className}
        children={
            items.map(
                (step) => <Swiper.Item {...step} />
            )
        }
        allowTouchMove={allowTouchMove}
        autoplay={autoplay}
        autoplayInterval={autoplayInterval}
        defaultIndex={defaultIndex}
        direction={direction}
        loop={loop}
        rubberband={rubberband}
        slideSize={slideSize}
        stuckAtBoundary={stuckAtBoundary}
        trackOffset={trackOffset}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }
    />;
};

MobileSwiper.propTypes = {
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
     * 用于定义内部各子项
     */
    items: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 必填，用于为当前子项设置唯一识别id
             */
            key: PropTypes.string.isRequired,

            /**
             * 用于为当前子项设置内部元素
             */
            children: PropTypes.node
        })
    ),

    /**
     * 用于为当前走马灯组件设置是否允许手势滑动
     * 默认：true
     */
    allowTouchMove: PropTypes.bool,

    /**
     * 用于为当前走马灯组件设置是否自动切换
     * 默认：false
     */
    autoplay: PropTypes.bool,

    /**
     * 用于为当前走马灯组件设置自动切换时间间隔，单位：毫秒
     * 默认：3000
     */
    autoplayInterval: PropTypes.number,

    /**
     * 用于为当前走马灯设置初始展示的子项位序（从0开始计数）
     * 默认：0
     */
    defaultIndex: PropTypes.number,

    /**
     * 用于为当前走马灯设置显示方向
     * 可选的有'horizontal'、'vertical'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * 用于为当前走马灯设置是否循环轮播
     * 默认：false
     */
    loop: PropTypes.bool,

    /**
     * 用于为当前走马灯设置是否在拖动超出内容区域时启用橡皮筋效果
     * 仅在非loop模式下可用
     * 默认：true
     */
    rubberband: PropTypes.bool,

    /**
     * 用于为当前走马灯设置滑块的宽度百分比
     * 默认：100
     */
    slideSize: PropTypes.number,

    /**
     * 用于为当前走马灯设置是否在边界两边卡住，避免出现空白
     * 仅在非loop模式下且slideSize<100时生效
     * 默认：true
     */
    stuckAtBoundary: PropTypes.bool,

    /**
     * 用于为当前走马灯设置滑块轨道整体的偏移量百分比
     * 默认：0
     */
    trackOffset: PropTypes.number,

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

MobileSwiper.defaultProps = {
    items: [],
    allowTouchMove: true,
    autoplay: false,
    autoplayInterval: 3000,
    defaultIndex: 0,
    direction: 'horizontal',
    loop: false,
    rubberband: true,
    slideSize: 100,
    stuckAtBoundary: true,
    trackOffset: 0
};

export default React.memo(MobileSwiper);