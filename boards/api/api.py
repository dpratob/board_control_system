from rest_framework.decorators import api_view
from rest_framework.response import Response
from boards.models import Board, BoardFeature
from boards.api.serializers import BoardSerializer, BoardFeatureSerializer

@api_view(['GET'])
def board_api_view(request):
    
    if request.method == 'GET':
        boards = Board.objects.all()
        board_serializer = BoardSerializer(boards, many = True)
        return Response(board_serializer.data)


@api_view(['GET'])
def board_feature_api_view(request):

    if request.method == 'GET':
        board_features = BoardFeature.objects.all()
        board_feature_serializer = BoardFeatureSerializer(board_features, many=True)
        return Response(board_feature_serializer.data)