from django.urls import path, include
from .views import ProfileDetail

urlpatterns = [
    path('profile/', ProfileDetail.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
]
