from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request, "automator/home.html")

    def post(self, request):
        return render(request, "automator/home.html")
