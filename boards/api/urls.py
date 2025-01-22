from django.urls import path
from boards.api.api import (
    board_api_view, board_detail_api_view,
    board_feature_api_view, board_feature_detail_api_view,
    board_publication_api_view, board_publication_detail_api_view,
    event_api_view, event_detail_api_view,
    group_api_view, group_detail_api_view,
    user_api_view, user_detail_api_view
)

urlpatterns = [
    
    # Board API
    path('board/', board_api_view, name = 'board_api'),
    path('board/<int:pk>/', board_detail_api_view, name = 'board_detail_api'),

    # Board Feature API
    path('board_feature/', board_feature_api_view, name = 'board_feature_api'),
    path('board_feature/<int:pk>/', board_feature_detail_api_view, name = 'board_feature_detail_api'),

    # Board Publication API
    path('board_publication/', board_publication_api_view, name = 'board_publication_api'),
    path('board_publication/<int:pk>/', board_publication_detail_api_view, name = 'board_publication_detail_api'),
    
    # Event API
    path('event/', event_api_view, name = 'event_api'),
    path('event/<int:pk>/', event_detail_api_view, name = 'event_detail_api'),

    # Group API
    path('group/', group_api_view, name = 'group_api'),
    path('group/<int:pk>/', group_detail_api_view, name = 'group_detail_api'),

    # User API
    path('user/', user_api_view, name = 'user_api'),
    path('user/<int:pk>/', user_detail_api_view, name = 'user_detail_api'),
]
