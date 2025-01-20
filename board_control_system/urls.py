from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boards.api.urls')),
    path('board_feature/', include('boards.api.urls')),
    path('board_publication/', include('boards.api.urls')),
    path('event/', include('boards.api.urls')),
    path('group/', include('boards.api.urls')),
    path('repetition/', include('boards.api.urls')),
    path('user/', include('boards.api.urls')),
]
