from rest_framework.response import Response
from rest_framework.views import APIView
from boards.models import Board
from boards.api.serializers import BoardSerializer

class BoardAPIView(APIView):
    
    def get(self, request):
        boards = Board.objects.all()
        board_serializer = BoardSerializer(boards, many = True)
        return Response(board_serializer.data)
