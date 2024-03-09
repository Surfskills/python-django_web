from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('', include("users.urls")),
    path('api-auth', include("rest_framework.urls"))
    
]
