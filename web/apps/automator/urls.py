from django.urls import path

from apps.automator.views import HomePage

urlpatterns = [
    path("", HomePage.as_view()),
]
