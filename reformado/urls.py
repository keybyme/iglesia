
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('rv60app.urls')),
    path('search/', include('search.urls')),
    path('menu/', include('menu.urls')),
]