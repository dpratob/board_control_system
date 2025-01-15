from django.urls import path
from boards.api.api import BoardAPIView

urlpatterns = [
    path('board/', BoardAPIView.as_view(), name = 'board_api'),
]
