from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('account/', include(users_urls)),
]
