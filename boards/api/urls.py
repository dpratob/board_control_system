from django.urls import path
from boards.api.api import board_api_view, board_feature_api_view, board_publication_api_view

urlpatterns = [
    path('board/', board_api_view, name = 'board_api'),
    path('board_feature/', board_feature_api_view, name = 'board_feature_api'),
    path('board_publication/', board_publication_api_view, name = 'board_publication_api'),
]
