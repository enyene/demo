from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def api(request):
    data = {
        "slackUsername":'iEnyene',
        "backend":True,
        "age":23,
        "bio":'am a backend developer'  
        }
    return JsonResponse(data)