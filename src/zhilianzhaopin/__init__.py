from typing import Any, List
from zhilianzhaopin.entity.ResumeSearchMajorNameCapi import ResumeSearchMajorNameCapiEntity
from zhilianzhaopin.entity.ZPWSOccupationalSearchResult import ZPWSOccupationalSearchResult
from zhilianzhaopin.entity.ZPWSSearchResult import ZPWSSearchResult
from zhilianzhaopin.entity.ResumeSearchSchoolNameCapiEntity import ResumeSearchSchoolNameCapiEntity
from zhilianzhaopin.entity.ResumeSearchCompanyNameCapi import ResumeSearchCompanyNameCapi
from utils.request import request
class APIRouter:
    cgateHost = "https://cgate.zhaopin.com"
    capiHost = "https://capi.zhaopin.com"

    def __init__(self, dev: bool=False):
        if(dev):
            self.capiHost = "https://capipre.zhaopin.com" 
            self.cgateHost = " https://cgate-pre.zhaopin.com"


API_ROOT = APIRouter()


def getReport(keyword: str="", dictType: str=""):
    # cgateHost + "/extapi/new-dict-service/dictReport"
    request()


def getDictVersion(**kwargs):
    # cgateHost + "/extapi/new-dict-service/getDictVersion"
    pass


def jobTitleFuzzyMatch(
        keyword: str,
        size: str,
        **kwargs) -> "ZPWSSearchResult":
    api = f"{API_ROOT.capiHost}/capi/resume/jobTitleFuzzyMatch"
    return request(api,params=kwargs)


def matchMultipleParentJobType(
    keyword: str,
    scene: str,
    **kwargs
) -> "ZPWSOccupationalSearchResult":
    #  cgateHost + "/resumeapi/searchv2/matchMultipleParentJobType"
    api = ""
    return request(api, kwargs)


def industryFuzzyMatch(
    keyword: str,
    size: str,
    **kwargs
)->"ZPWSSearchResult":
    api = f"{API_ROOT.capiHost}/capi/resume/industryFuzzyMatch"
    return request(api=api,params=kwargs)


def matchMultipleParentIndustry(keyword: str, **kwargs) -> Any:
    api = f"{API_ROOT.cgateHost}/resumeapi/searchv2/matchMultipleParentIndustry"
    return request(api, params=kwargs)


def languageCertificateImagine(
        searchWord: str,
        languageId: str,
        **kwargs
    ) -> "ZPWSSearchResult":
    api = f"{API_ROOT.capiHost}/capi/resume/languageCertificateImagine"
    return request(api, kwargs)


def dictReport(
        keyword: str,
        dictType: str,
        **kwargs):
    api = f"{API_ROOT.capiHost}/extapi/new-dict-service/dictReport"
    return request(api, kwargs)


def searchSkillTagByWord(
    jobTypeCode: str,
    word: str,
    scene: str,
    userRole: str,
    platform: str="4",
    **kwargs
):
    api = f"{API_ROOT.cgateHost}/extapi/new-dict-service/searchSkillTagByWord"
    return request(api, kwargs)


def registerSkillTag(
    tagValue: str,
    source: str,
    scene: str,
    userRole: str,
    platform: str="4",
    **kwargs
):
    api = f"{API_ROOT.cgateHost}/extapi/new-dict-service/registerSkillTag"
    return request(api, params=kwargs)


def schoolMatch(keyword: str, **kwargs) -> "ResumeSearchSchoolNameCapiEntity":
    api = f"{API_ROOT.cgateHost}/resumeapi/businessservice/schoolMatch"
    return request(api, kwargs)


def majorMatch(
        keyword: str,
        **kwargs) -> "ResumeSearchMajorNameCapiEntity":
    api = f"{API_ROOT.cgateHost}/resumeapi/businessservice/majorMatch"
    return request(api, params=kwargs)


def companyMatch(
    keyword:str,
    **kwargs
    )->"ResumeSearchCompanyNameCapi":
    api = f"{API_ROOT.cgateHost}/resumeapi/businessservice/companyMatch"
    return request(api,params=kwargs)
class Company:
    @staticmethod
    def visitCompanyFilter(
        enterpriseNameList:List[str]
    ):
        api = f"{API_ROOT.cgateHost}/mbTalent/zhima-credit/visitCompanyFilter"
    @staticmethod
    def isFocus(
        rootId:str
    ):
        api = f"{API_ROOT.capiHost}/capi/live/isFocus"
    @staticmethod
    def companyDetail(
        number:str,
        indexFilterCity:str,
        **kwargs
    ):
        api = f"{API_ROOT.cgateHost}/positionbusiness/exposure/companyDetail"
        request(api,kwargs)
    @staticmethod
    def cancelCompanyCollect():
        api = f"{API_ROOT.cgateHost}/behavior/userforward/cancelCompanyCollect"
        pass
    @staticmethod
    def companyInfoQuery(
        enterpriseName:str,
        fromAssociation:bool,
        size:int = 10,
        **kwargs
    ):
        api = f"{API_ROOT.cgateHost}/mbTalent/zhima-credit/companyInfoQuery"
        return request(api,kwargs)
    @staticmethod
    def getCompanyExtDetail(
        companyNumber:str,
        sourceType:str,
        companyName:str,
        information:str = "true",
        competitvePower:str = "true",
        atlas:str ="1",
        **kwargs
        ):
        api = f"{API_ROOT.cgateHost}/riskstorm/company/getCompanyExtDetail"
        pass
    @staticmethod
    def companySearch(
        filter_c_fullIndex:str = "",
        ranking_c_workCity:str = "489",
        filter_c_company_size ="",
        filter_c_company_type ="",
        filter_c_industryId ="",
        cvNumber="",
        pageCode ="5019",
        pageIndex = 1,
        pageSize = 20,
        eventScenario="searchCompanyListNative",
    ):
        api = f"{API_ROOT.capiHost}/capi/search/companySearch"
        params = {
            "filter_c_fullIndex": filter_c_fullIndex,
            "ranking_c_workCity": ranking_c_workCity,
            "filter_c_company_size":filter_c_company_size,
            "filter_c_company_type":filter_c_company_type,
            "filter_c_industryId":filter_c_industryId,
            "cvNumber":cvNumber,
            "pageCode":pageCode,
            "pageIndex":pageIndex,
            "pageSize":pageSize,
            "eventScenario":eventScenario,
        }
        return request(api,params=params)
    @staticmethod
    def addCompanyCollect(
        numbers:str
    ):
        api = f"{API_ROOT.cgateHost}/behavior/userforward/addCompanyCollect"
        pass
