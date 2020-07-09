from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('', views.get_self_profile, name='profile'),
]