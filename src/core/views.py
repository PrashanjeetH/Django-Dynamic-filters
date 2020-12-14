from django.shortcuts import render

# Create your views here.


def BootstrapFilterView(request):
    return render(request, "index.html", {})