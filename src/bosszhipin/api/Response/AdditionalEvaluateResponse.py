from bosszhipin.api.Response.HttpResponse import HttpResponse


class AdditionalEvaluateResponse(HttpResponse):
    serialVersionUID = 8614501089253074264
    additionalQuestion: "AdditionalQuestionBean"