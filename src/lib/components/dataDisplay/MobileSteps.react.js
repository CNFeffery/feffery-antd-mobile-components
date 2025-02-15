/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { Steps } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 步骤条组件MobileSteps
 */
const MobileSteps = ({
    id,
    key,
    style,
    className,
    steps = [],
    current = 0,
    direction = 'horizontal',
    setProps
}) => {

    return <Steps
        id={id}
        key={key}
        style={style}
        className={className}
        current={current}
        direction={direction}
        children={
            steps.map(
                (step) => <Steps.Step {...step} />
            )
        }
        data-dash-is-loading={useLoading()}
    />;
};

MobileSteps.propTypes = {
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
     * 用于定义内部各步骤
     */
    steps: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 用于设置当前步骤的详情描述内容
             */
            description: PropTypes.node,

            /**
             * 用于设置当前步骤的图标内容
             */
            icon: PropTypes.node,

            /**
             * 用于指定当前步骤的状态
             * 可选的有'wait'、'process'、'finish'、'error'
             * 当不设置时，会自动根据current来指定状态
             * 默认：'wait'
             */
            status: PropTypes.oneOf(['wait', 'process', 'finish', 'error']),

            /**
             * 用于设置当前步骤的标题内容
             */
            title: PropTypes.node
        })
    ),

    /**
     * 用于设置当前步骤条所在步骤（从0开始计数）
     * 默认：0
     */
    current: PropTypes.number,

    /**
     * 用于设置步骤条显示方向
     * 可选的有'horizontal'、'vertical'
     * 默认：'horizontal'
     */
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileSteps);