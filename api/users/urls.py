from django.urls import path, include
from .views import ProfileDetail

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('profile/', ProfileDetail.as_view()),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

