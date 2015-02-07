from django.shortcuts import render

# Create your views here.
def sample_app_view(request):
    return render(request, "sample_app/sample_app.html")