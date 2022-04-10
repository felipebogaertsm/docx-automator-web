from django.urls import path

from apps.automator.views import home_page

urlpatterns = [
    path("", home_page),
]
