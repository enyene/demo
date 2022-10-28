from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def api(request):
    data = {
        "slackUsername":'iEnyene',
        "backend":True,
        "age":23,
        "bio":'am a backend developer'  
        }
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response