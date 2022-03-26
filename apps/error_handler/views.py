from django.shortcuts import render

# Create your views here.
def error_404(request, exception):
    data = {}
    return render(request, 'error_pages/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_pages/500.html', data)

def error_403(request, exception):
    data = {}
    return render(request, 'error_pages/403.html', data)

def error_400(request, exception):
    data = {}
    return render(request, 'error_pages/403.html', data)