/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import { SafeArea } from 'antd-mobile';
// 辅助库
import { useLoading } from '../../utils';


/**
 * 安全区组件MobileSafeArea
 */
const MobileSafeArea = ({
    id,
    position,
    setProps
}) => {

    return <SafeArea
        id={id}
        position={position}
        data-dash-is-loading={useLoading()}
    />;
};

MobileSafeArea.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 安全区位置，可选项有`'top'`、`'bottom'`
     */
    position: PropTypes.oneOf(['top', 'bottom']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(MobileSafeArea);