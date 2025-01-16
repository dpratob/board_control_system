from django.urls import path
from boards.api.api import board_api_view, board_feature_api_view, board_publication_api_view, event_api_view, group_api_view, interaction_api_view, publication_api_view, publication_type_api_view, repetition_api_view, user_api_view

urlpatterns = [
    path('board/', board_api_view, name = 'board_api'),
    path('board_feature/', board_feature_api_view, name = 'board_feature_api'),
    path('board_publication/', board_publication_api_view, name = 'board_publication_api'),
    path('event/', event_api_view, name = 'event_api'),
    path('group/', group_api_view, name = 'group_api'),
    path('interaction/', interaction_api_view, name = 'interaction_api'),
    path('publication/', publication_api_view, name = 'publication_api'),
    path('publication_type/', publication_type_api_view, name = 'publication_type_api'),
    path('repetition/', repetition_api_view, name = 'repetition_api'),
    path('user/', user_api_view, name = 'user_api'),
]
