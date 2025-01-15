from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boards.api.urls')),
    path('board_feature/', include('boards.api.urls')),
    path('board_publication/', include('boards.api.urls')),
]
