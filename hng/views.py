from django.http import JsonResponse


def api(request):
    data = {
        "slackUsername":'iEnyene',
        "backend":True,
        "age":23,
        "bio":'am a backend developer'  
        }
    return JsonResponse(data)