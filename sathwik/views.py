from .models import Users, ActivityPeriod
from django.http import JsonResponse


# Create your views here.
def retrieve(request):
    user_result = list(Users.objects.values('id', 'real_name', 'tz'))
    list_activity = []
    for i in user_result:
        b = list(ActivityPeriod.objects.filter(aid=i['id']).values('start_time', 'end_time'))
        i.update({'activity_periods': b})
        list_activity.append(i)
    return JsonResponse({"ok":  True, 'members': list_activity})
