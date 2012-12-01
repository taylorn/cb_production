from myproject import settings

def assign_sidebar(request):
    if request.path in settings.SIDEBAR_URLS:
        return {'sidebar_on': True}
    else:
        return {'sidebar_on': False}
