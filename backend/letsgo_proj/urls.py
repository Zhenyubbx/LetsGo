from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('letsgo_api/', include('letsgo_api.urls')),
    path('auth/', obtain_auth_token),
]
