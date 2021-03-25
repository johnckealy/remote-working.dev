from django.urls import path
from .views import JobsIndex

urlpatterns = [
    path('jobs/', JobsIndex.as_view()),
]

