/* eslint-disable no-undefined */
/* eslint-disable no-unused-vars */
/* eslint-disable no-empty */
/* eslint-disable no-magic-numbers */
/* eslint-disable prefer-const */
// react核心
import React from 'react';
import PropTypes from 'prop-types';
// antd核心
import {
    AddCircleOutline,
    AddOutline,
    AddSquareOutline,
    AppOutline,
    AppstoreOutline,
    ArrowDownCircleOutline,
    ArrowsAltOutline,
    BankcardOutline,
    BellMuteOutline,
    BellOutline,
    BillOutline,
    CalculatorOutline,
    CalendarOutline,
    CheckCircleOutline,
    CheckOutline,
    CheckShieldOutline,
    ClockCircleOutline,
    CloseCircleOutline,
    CloseOutline,
    CompassOutline,
    ContentOutline,
    DeleteOutline,
    DownCircleOutline,
    DownOutline,
    DownlandOutline,
    EditSOutline,
    EnvironmentOutline,
    ExclamationCircleOutline,
    ExclamationOutline,
    ExclamationShieldOutline,
    ExclamationTriangleOutline,
    EyeInvisibleOutline,
    EyeOutline,
    FileOutline,
    FillinOutline,
    FilterOutline,
    FingerdownOutline,
    FlagOutline,
    FolderOutline,
    GlobalOutline,
    HeartOutline,
    HistogramOutline,
    InformationCircleOutline,
    LeftOutline,
    LikeOutline,
    LinkOutline,
    LocationOutline,
    LockOutline,
    LoopOutline,
    MailOpenOutline,
    MailOutline,
    MessageOutline,
    MinusCircleOutline,
    MinusOutline,
    MoreOutline,
    PayCircleOutline,
    PictureOutline,
    PicturesOutline,
    PieOutline,
    PlayOutline,
    QuestionCircleOutline,
    RedoOutline,
    RightOutline,
    SearchOutline,
    SendOutline,
    SetOutline,
    ShopbagOutline,
    ShrinkOutline,
    StarOutline,
    StopOutline,
    SystemQRcodeOutline,
    TagOutline,
    TeamOutline,
    TextDeletionOutline,
    TextOutline,
    UndoOutline,
    UnlockOutline,
    UnorderedListOutline,
    UpCircleOutline,
    UpOutline,
    UploadOutline,
    UserAddOutline,
    UserCircleOutline,
    UserContactOutline,
    UserOutline,
    UserSetOutline,
    VideoOutline
} from 'antd-mobile-icons';

// 图标代号 -> 图表组件映射
const iconDict = new Map([
    ['AddCircleOutline', AddCircleOutline],
    ['AddOutline', AddOutline],
    ['AddSquareOutline', AddSquareOutline],
    ['AppOutline', AppOutline],
    ['AppstoreOutline', AppstoreOutline],
    ['ArrowDownCircleOutline', ArrowDownCircleOutline],
    ['ArrowsAltOutline', ArrowsAltOutline],
    ['BankcardOutline', BankcardOutline],
    ['BellMuteOutline', BellMuteOutline],
    ['BellOutline', BellOutline],
    ['BillOutline', BillOutline],
    ['CalculatorOutline', CalculatorOutline],
    ['CalendarOutline', CalendarOutline],
    ['CheckCircleOutline', CheckCircleOutline],
    ['CheckOutline', CheckOutline],
    ['CheckShieldOutline', CheckShieldOutline],
    ['ClockCircleOutline', ClockCircleOutline],
    ['CloseCircleOutline', CloseCircleOutline],
    ['CloseOutline', CloseOutline],
    ['CompassOutline', CompassOutline],
    ['ContentOutline', ContentOutline],
    ['DeleteOutline', DeleteOutline],
    ['DownCircleOutline', DownCircleOutline],
    ['DownOutline', DownOutline],
    ['DownlandOutline', DownlandOutline],
    ['EditSOutline', EditSOutline],
    ['EnvironmentOutline', EnvironmentOutline],
    ['ExclamationCircleOutline', ExclamationCircleOutline],
    ['ExclamationOutline', ExclamationOutline],
    ['ExclamationShieldOutline', ExclamationShieldOutline],
    ['ExclamationTriangleOutline', ExclamationTriangleOutline],
    ['EyeInvisibleOutline', EyeInvisibleOutline],
    ['EyeOutline', EyeOutline],
    ['FileOutline', FileOutline],
    ['FillinOutline', FillinOutline],
    ['FilterOutline', FilterOutline],
    ['FingerdownOutline', FingerdownOutline],
    ['FlagOutline', FlagOutline],
    ['FolderOutline', FolderOutline],
    ['GlobalOutline', GlobalOutline],
    ['HeartOutline', HeartOutline],
    ['HistogramOutline', HistogramOutline],
    ['InformationCircleOutline', InformationCircleOutline],
    ['LeftOutline', LeftOutline],
    ['LikeOutline', LikeOutline],
    ['LinkOutline', LinkOutline],
    ['LocationOutline', LocationOutline],
    ['LockOutline', LockOutline],
    ['LoopOutline', LoopOutline],
    ['MailOpenOutline', MailOpenOutline],
    ['MailOutline', MailOutline],
    ['MessageOutline', MessageOutline],
    ['MinusCircleOutline', MinusCircleOutline],
    ['MinusOutline', MinusOutline],
    ['MoreOutline', MoreOutline],
    ['PayCircleOutline', PayCircleOutline],
    ['PictureOutline', PictureOutline],
    ['PicturesOutline', PicturesOutline],
    ['PieOutline', PieOutline],
    ['PlayOutline', PlayOutline],
    ['QuestionCircleOutline', QuestionCircleOutline],
    ['RedoOutline', RedoOutline],
    ['RightOutline', RightOutline],
    ['SearchOutline', SearchOutline],
    ['SendOutline', SendOutline],
    ['SetOutline', SetOutline],
    ['ShopbagOutline', ShopbagOutline],
    ['ShrinkOutline', ShrinkOutline],
    ['StarOutline', StarOutline],
    ['StopOutline', StopOutline],
    ['SystemQRcodeOutline', SystemQRcodeOutline],
    ['TagOutline', TagOutline],
    ['TeamOutline', TeamOutline],
    ['TextDeletionOutline', TextDeletionOutline],
    ['TextOutline', TextOutline],
    ['UndoOutline', UndoOutline],
    ['UnlockOutline', UnlockOutline],
    ['UnorderedListOutline', UnorderedListOutline],
    ['UpCircleOutline', UpCircleOutline],
    ['UpOutline', UpOutline],
    ['UploadOutline', UploadOutline],
    ['UserAddOutline', UserAddOutline],
    ['UserCircleOutline', UserCircleOutline],
    ['UserContactOutline', UserContactOutline],
    ['UserOutline', UserOutline],
    ['UserSetOutline', UserSetOutline],
    ['VideoOutline', VideoOutline],
])

/**
 * 图标组件MobileIcon
 */
const MobileIcon = (props) => {
    let {
        id,
        key,
        style,
        className,
        icon,
        nClicks,
        loading_state,
        setProps
    } = props;

    return (
        iconDict.get(icon) ?
            React.createElement(
                iconDict.get(icon),
                {
                    id: id,
                    key: key,
                    style: {
                        verticalAlign: 'middle',
                        ...style
                    },
                    className: className,
                    onClick: () => setProps({ nClicks: nClicks + 1 }),
                    'data-dash-is-loading': (loading_state && loading_state.is_loading) || undefined
                }
            ) :
            null
    );
};

MobileIcon.propTypes = {
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
     * 用于设置当前所使用的图标代号
     */
    icon: PropTypes.string.isRequired,

    // 组件监听类属性
    /**
     * 用于记录当前图标累计被点击次数
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

MobileIcon.defaultProps = {
    nClicks: 0
};

export default React.memo(MobileIcon);