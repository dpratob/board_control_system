from django.urls import path
from boards.api.api import board_api_view

urlpatterns = [
    path('board/', board_api_view, name = 'board_api'),
]
