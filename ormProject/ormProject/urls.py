from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ormApp.urls')),
    path('admin/', admin.site.urls),
]