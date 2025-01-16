from rest_framework.decorators import api_view
from rest_framework.response import Response
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, Interaction, Publication, PublicationType, Repetition, User
from boards.api.serializers import BoardSerializer, BoardFeatureSerializer, BoardPublicationSerializer, EventSerializer, GroupSerializer, InteractionSerializer, PublicationSerializer, PublicationTypeSerializer, RepetitionSerializer, UserSerializer

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


@api_view(['GET'])
def board_publication_api_view(request):

    if request.method == 'GET':
        board_publications = BoardPublication.objects.all()
        board_publication_serializer = BoardPublicationSerializer(board_publications, many=True)
        return Response(board_publication_serializer.data)


@api_view(['GET'])
def event_api_view(request):

    if request.method == 'GET':
        events = Event.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return Response(event_serializer.data)


@api_view(['GET'])
def group_api_view(request):

    if request.method == 'GET':
        groups = Group.objects.all()
        group_serializer = GroupSerializer(groups, many=True)
        return Response(group_serializer.data)


@api_view(['GET'])
def interaction_api_view(request):

    if request.method == 'GET':
        interactions = Interaction.objects.all()
        interaction_serializer = InteractionSerializer(interactions, many=True)
        return Response(interaction_serializer.data)


@api_view(['GET'])
def publication_api_view(request):

    if request.method == 'GET':
        publications = Publication.objects.all()
        publication_serializer = PublicationSerializer(publications, many=True)
        return Response(publication_serializer.data)


@api_view(['GET'])
def publication_type_api_view(request):

    if request.method == 'GET':
        publication_types = PublicationType.objects.all()
        publication_type_serializer = PublicationTypeSerializer(publication_types, many=True)
        return Response(publication_type_serializer.data)


@api_view(['GET'])
def repetition_api_view(request):

    if request.method == 'GET':
        repetitions = Repetition.objects.all()
        repetition_serializer = RepetitionSerializer(repetitions, many=True)
        return Response(repetition_serializer.data)


@api_view(['GET'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)
