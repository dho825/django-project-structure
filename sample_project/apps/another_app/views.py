from django.shortcuts import render

# Create your views here.
def another_app_view(request):
    return render(request, "another_app/another_app.html")