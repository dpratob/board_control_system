from rest_framework.decorators import api_view
from rest_framework.response import Response
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, Interaction, Publication, PublicationType, Repetition, User
from boards.api.serializers import BoardSerializer, BoardFeatureSerializer, BoardPublicationSerializer, EventSerializer, GroupSerializer, InteractionSerializer, PublicationSerializer, PublicationTypeSerializer, RepetitionSerializer, UserSerializer

@api_view(['GET', 'POST'])
def board_api_view(request):
    
    # Get all boards
    if request.method == 'GET':
        boards = Board.objects.all()
        board_serializer = BoardSerializer(boards, many = True)
        return Response(board_serializer.data)

    # Create a new board
    elif request.method == 'POST':
        board_serializer = BoardSerializer(data = request.data)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data)
        return Response(board_serializer.errors)


@api_view(['GET', 'POST'])
def board_feature_api_view(request):

    # Get all board features
    if request.method == 'GET':
        board_features = BoardFeature.objects.all()
        board_feature_serializer = BoardFeatureSerializer(board_features, many=True)
        return Response(board_feature_serializer.data)

    # Create a new board feature
    elif request.method == 'POST':
        board_feature_serializer = BoardFeatureSerializer(data=request.data)
        if board_feature_serializer.is_valid():
            board_feature_serializer.save()
            return Response(board_feature_serializer.data)
        return Response(board_feature_serializer.errors)


@api_view(['GET', 'POST'])
def board_publication_api_view(request):

    # Get all board publications
    if request.method == 'GET':
        board_publications = BoardPublication.objects.all()
        board_publication_serializer = BoardPublicationSerializer(board_publications, many=True)
        return Response(board_publication_serializer.data)

    # Create a new board publication
    elif request.method == 'POST':
        board_publication_serializer = BoardPublicationSerializer(data=request.data)
        if board_publication_serializer.is_valid():
            board_publication_serializer.save()
            return Response(board_publication_serializer.data)
        return Response(board_publication_serializer.errors)


@api_view(['GET', 'POST'])
def event_api_view(request):

    # Get all events
    if request.method == 'GET':
        events = Event.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return Response(event_serializer.data)
    
    # Create a new event
    elif request.method == 'POST':
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data)
        return Response(event_serializer.errors)


@api_view(['GET', 'POST'])
def group_api_view(request):

    # Get all groups
    if request.method == 'GET':
        groups = Group.objects.all()
        group_serializer = GroupSerializer(groups, many=True)
        return Response(group_serializer.data)
    
    # Create a new group
    elif request.method == 'POST':
        group_serializer = GroupSerializer(data=request.data)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data)
        return Response(group_serializer.errors)


@api_view(['GET', 'POST'])
def interaction_api_view(request):

    # Get all interactions
    if request.method == 'GET':
        interactions = Interaction.objects.all()
        interaction_serializer = InteractionSerializer(interactions, many=True)
        return Response(interaction_serializer.data)
    
    # Create a new interaction
    elif request.method == 'POST':
        interaction_serializer = InteractionSerializer(data=request.data)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return Response(interaction_serializer.data)
        return Response(interaction_serializer.errors)


@api_view(['GET', 'POST'])
def publication_api_view(request):

    # Get all publications
    if request.method == 'GET':
        publications = Publication.objects.all()
        publication_serializer = PublicationSerializer(publications, many=True)
        return Response(publication_serializer.data)
    
    # Create a new publication
    elif request.method == 'POST':
        publication_serializer = PublicationSerializer(data=request.data)
        if publication_serializer.is_valid():
            publication_serializer.save()
            return Response(publication_serializer.data)
        return Response(publication_serializer.errors)


@api_view(['GET', 'POST'])
def publication_type_api_view(request):

    # Get all publication types
    if request.method == 'GET':
        publication_types = PublicationType.objects.all()
        publication_type_serializer = PublicationTypeSerializer(publication_types, many=True)
        return Response(publication_type_serializer.data)
    
    # Create a new publication type
    elif request.method == 'POST':
        publication_type_serializer = PublicationTypeSerializer(data=request.data)
        if publication_type_serializer.is_valid():
            publication_type_serializer.save()
            return Response(publication_type_serializer.data)
        return Response(publication_type_serializer.errors)


@api_view(['GET', 'POST'])
def repetition_api_view(request):

    # Get all repetitions
    if request.method == 'GET':
        repetitions = Repetition.objects.all()
        repetition_serializer = RepetitionSerializer(repetitions, many=True)
        return Response(repetition_serializer.data)
    
    # Create a new repetition
    elif request.method == 'POST':
        repetition_serializer = RepetitionSerializer(data=request.data)
        if repetition_serializer.is_valid():
            repetition_serializer.save()
            return Response(repetition_serializer.data)
        return Response(repetition_serializer.errors)


@api_view(['GET', 'POST'])
def user_api_view(request):

    # Get all users
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)
    
    # Create a new user
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
