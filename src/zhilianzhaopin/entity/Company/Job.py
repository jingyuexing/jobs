from typing import Any, List

from pydantic import BaseModel
from zhilianzhaopin.entity.CapiBase import CapiBase

class CompanyRanking:
    name:str
    rankingType:str
    url:str


class DataBean(BaseModel):
    adId:str
    appDownloadUrl:str
    appName:str
    exposeId:str
    exposureUrls:List[str]
    hasJdlistadverexposed:bool
    height:str
    imageId:str
    invokeApp:bool
    invokePackageName:str
    invokeSchema:str
    link:str
    mediaType:int
    proData:Any
    tabIndex:int
    thirdPartyDsp:bool
    url:str
    width:str

class ExposureCompany(BaseModel):
    companyName:str
    companyNumber:str
    state:int

class ExtensionsBean(BaseModel):
    operationExtension:"OperationExtensionBean"
class KongShuangModelDTO(BaseModel):
    pass
class CampusFeedOperationCardData(BaseModel):
    pass
class CampusFeedPositionCardData(BaseModel):
    pass
class KongXuanModelDTO(BaseModel):
    pass
class LiveCard(BaseModel):
    pass
class LiveModelDTO(BaseModel):
    pass
class MatchInfoBean(BaseModel):
    pass

class CommercialLabel(BaseModel):
    pass
class PositionNpsBean(BaseModel):
    pass
class VideoInfo:
    pass
class ProxyModelBean:
    pass
class RecallSignBean:
    pass
class SkillLabelBean:
    pass
class Staff:
    pass
class BaseLabelInfo(BaseModel):
    pass
class ExplainBean(BaseModel):
    label:str
    sourceUrl:str
    type:int
    videoId:int

class HighLightBean(BaseModel):
    positionHighlight:str
class LiveBean:
    icon:str
    liveState:int
    liveTips:str
    roomId:int
    startTimeFormat:str
    videoUrl:str

class OrgBestListRanking:
    bestListJumpUrl:str
    electOfficial:str
    iconUrl:str
    listType:str
    reason:str
    settleTime:str
    value:str
class ReportData(BaseModel):
    bizid:str

class RankingBean(BaseModel):
    rankIcon:str
    rankName:str
    rankType:str
    rankTypeName:str
    reportData:"ReportData"

class RecommendReasonBean(BaseModel):
    label:str
    reason:str

class OperationExtensionBean(BaseModel):
    explain:"ExplainBean"
    highlight:"HighLightBean"
    live:"LiveBean"
    liveRoomState:str
    liveVideoState:str
    orgBestListRanking:"OrgBestListRanking"
    ranking:"RankingBean"
    recommendReason:"RecommendReasonBean"
    type:int


class Job(CapiBase):
    serialVersionUID = 1;
    MenVipUrl1709:str
    actionId:str
    applyType:str
    batchDeliveryType:int
    canBeRegular:bool
    canRemoteInternship:bool
    cardType:int
    chatWindow:int
    choiceValue:bool
    cityDistrict:str
    cityId:str
    collectTime:str
    companyId:int
    companyLogo:str
    companyName:str
    companyNumber:str
    companyRankings:List["CompanyRanking"]
    companyRootId:str
    companyScaleTypeTagsNew:List[str]
    companySize:str
    companyUrl:str
    data:Any
    dataBean:"DataBean";
    deliveryPath:str
    distance:float
    distanceFormat:str
    education:str
    exposureData:"ExposureCompany"
    extensions:"ExtensionsBean"
    feedOperation:"CampusFeedOperationCardData"
    feedPosition:"CampusFeedPositionCardData"
    funczone:str
    # @JSONField(alternateNames = {"isApplied", "hasAppliedPosition"})
    hasAppliedPosition:bool
    hasVjdexposed:bool
    industryName:str
    internshipMonths:int
    isChatWindow:int
    isExpressDelivery:bool
    isFavirited:bool
    isFeedback:bool
    isJobRead:bool
    isNewPosition:int
    isRead:bool
    # @JSONField(alternateNames = {"jobId", "id"})
    jobId:int
    kongShuangModel:"KongShuangModelDTO"
    kongXuanModel:"KongXuanModelDTO"
    liveCard:"LiveCard"
    liveModel:"LiveModelDTO"
    mPos:int
    matchInfo:"MatchInfoBean"
    menVipLevel:int
    name:str
    needMajor:List[str]
    number:str
    pageCode:str
    positionCommercialLabel:List["CommercialLabel"]
    positionExpandCardData:str
    positionExpandCardType:int
    positionHighlight:str
    positionNpsBean:"PositionNpsBean"
    positionOfNlp:int
    positionSourceType:int
    positionSourceTypeUrl:str
    positionStatus:int
    positionURL:str
    positionVideoCard:List["VideoInfo"]
    proData:Any
    property:str
    propertyCode:str
    propertyType:str
    propertyTypeUrl:str
    provideInternshipCertificate:bool
    proxyModel:"ProxyModelBean"
    publishTime:str
    recallSign:"RecallSignBean"
    redirectUrl:str
    redirectable:bool
    rpoProxy:bool
    rsmno:str
    salary:str
    # @JSONField(alternateNames = {"salary60", "Salary60"})
    salary60:str
    salaryCount:str
    salaryReal:str
    settlementType:str
    showDistance:int
    showMsgTime:str
    skillLabel:List["SkillLabelBean"];
    sports:List[str]
    # @JSONField(alternateNames = {"staff", "staffCard"})
    staff:"Staff"
    streamStatus:str
    streetName:str
    subJobTypeLevel:str
    subJobTypeLevelName:str
    suggestionTitle:str
    suggestionTypeItem:List[str]
    svcarg:str
    tagABC:str
    tags:List[str]
    traceid:str
    tradingArea:str
    type:int
    viewResumeStatus:int
    weeklyInternshipDays:int
    # @JSONField(alternateNames = {"welfareLabel", "WelfareTab"})
    welfareLabel:List["BaseLabelInfo"]
    workCity:str
    workDateType:str
    workMode:str
    workType:str
    workingExp:str
    isClick = False;
    mHasReport = False;
    itemType = 0;
    itemStyleType = 0;
