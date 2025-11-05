from .models import Projects

def context_processor(request):
    allprojects = Projects.objects.order_by('-id')[:6]
    
    return {
        'ourprojects': allprojects,
    }