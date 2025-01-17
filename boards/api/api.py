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
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def board_detail_api_view(request, pk=None):
    
    # Get a single board
    if request.method == 'GET':
        board = Board.objects.filter(id=pk).first()
        board_serializer = BoardSerializer(board)
        return Response(board_serializer.data)
    
    # Update a single board completely
    elif request.method == 'PUT':
        board = Board.objects.filter(id=pk).first()
        board_serializer = BoardSerializer(board, data = request.data)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data)
        return Response(board_serializer.errors)
    
    # Update a single board partially
    elif request.method == 'PATCH':
        board = Board.objects.filter(id=pk).first()
        board_serializer = BoardSerializer(board, data = request.data, partial = True)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data)
        return Response(board_serializer.errors)

    # Delete a single board
    elif request.method == 'DELETE':
        board = Board.objects.filter(id=pk).first()
        board.delete()
        return Response({'message': 'Board deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def board_feature_detail_api_view(request, pk=None):
    
    # Get a single board feature
    if request.method == 'GET':
        board_feature = BoardFeature.objects.filter(id=pk).first()
        board_feature_serializer = BoardFeatureSerializer(board_feature)
        return Response(board_feature_serializer.data)

    # Update a single board feature completely
    elif request.method == 'PUT':
        board_feature = BoardFeature.objects.filter(id=pk).first()
        board_feature_serializer = BoardFeatureSerializer(board_feature, data=request.data)
        if board_feature_serializer.is_valid():
            board_feature_serializer.save()
            return Response(board_feature_serializer.data)
        return Response(board_feature_serializer.errors)
    
    # Update a single board feature partially
    elif request.method == 'PATCH':
        board_feature = BoardFeature.objects.filter(id=pk).first()
        board_feature_serializer = BoardFeatureSerializer(board_feature, data=request.data, partial=True)
        if board_feature_serializer.is_valid():
            board_feature_serializer.save()
            return Response(board_feature_serializer.data)
        return Response(board_feature_serializer.errors)

    # Delete a single board feature
    elif request.method == 'DELETE':
        board_feature = BoardFeature.objects.filter(id=pk).first()
        board_feature.delete()
        return Response({'message': 'Board feature deleted successfully!'})


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
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def board_publication_detail_api_view(request, pk=None):
    
    # Get a single board publication
    if request.method == 'GET':
        board_publication = BoardPublication.objects.filter(id=pk).first()
        board_publication_serializer = BoardPublicationSerializer(board_publication)
        return Response(board_publication_serializer.data)

    # Update a single board publication completely
    elif request.method == 'PUT':
        board_publication = BoardPublication.objects.filter(id=pk).first()
        board_publication_serializer = BoardPublicationSerializer(board_publication, data=request.data)
        if board_publication_serializer.is_valid():
            board_publication_serializer.save()
            return Response(board_publication_serializer.data)
        return Response(board_publication_serializer.errors)
    
    # Update a single board publication partially
    elif request.method == 'PATCH':
        board_publication = BoardPublication.objects.filter(id=pk).first()
        board_publication_serializer = BoardPublicationSerializer(board_publication, data=request.data, partial=True)
        if board_publication_serializer.is_valid():
            board_publication_serializer.save()
            return Response(board_publication_serializer.data)
        return Response(board_publication_serializer.errors)

    # Delete a single board publication
    elif request.method == 'DELETE':
        board_publication = BoardPublication.objects.filter(id=pk).first()
        board_publication.delete()
        return Response({'message': 'Board publication deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def event_detail_api_view(request, pk=None):
    
    # Get a single event
    if request.method == 'GET':
        event = Event.objects.filter(id=pk).first()
        event_serializer = EventSerializer(event)
        return Response(event_serializer.data)
    
    # Update a single event completely
    elif request.method == 'PUT':
        event = Event.objects.filter(id=pk).first()
        event_serializer = EventSerializer(event, data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data)
        return Response(event_serializer.errors)
    
    # Update a single event partially
    elif request.method == 'PATCH':
        event = Event.objects.filter(id=pk).first()
        event_serializer = EventSerializer(event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data)
        return Response(event_serializer.errors)
    
    # Delete a single event
    elif request.method == 'DELETE':
        event = Event.objects.filter(id=pk).first()
        event.delete()
        return Response({'message': 'Event deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def group_detail_api_view(request, pk=None):
    
    # Get a single group
    if request.method == 'GET':
        group = Group.objects.filter(id=pk).first()
        group_serializer = GroupSerializer(group)
        return Response(group_serializer.data)
    
    # Update a single group completely
    elif request.method == 'PUT':
        group = Group.objects.filter(id=pk).first()
        group_serializer = GroupSerializer(group, data=request.data)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data)
        return Response(group_serializer.errors)
    
    # Update a single group partially
    elif request.method == 'PATCH':
        group = Group.objects.filter(id=pk).first()
        group_serializer = GroupSerializer(group, data=request.data, partial=True)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data)
        return Response(group_serializer.errors)
    
    # Delete a single group
    elif request.method == 'DELETE':
        group = Group.objects.filter(id=pk).first()
        group.delete()
        return Response({'message': 'Group deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def interaction_detail_api_view(request, pk=None):
    
    # Get a single interaction
    if request.method == 'GET':
        interaction = Interaction.objects.filter(id=pk).first()
        interaction_serializer = InteractionSerializer(interaction)
        return Response(interaction_serializer.data)
    
    # Update a single interaction completely
    elif request.method == 'PUT':
        interaction = Interaction.objects.filter(id=pk).first()
        interaction_serializer = InteractionSerializer(interaction, data=request.data)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return Response(interaction_serializer.data)
        return Response(interaction_serializer.errors)
    
    # Update a single interaction partially
    elif request.method == 'PATCH':
        interaction = Interaction.objects.filter(id=pk).first()
        interaction_serializer = InteractionSerializer(interaction, data=request.data, partial=True)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return Response(interaction_serializer.data)
        return Response(interaction_serializer.errors)

    # Delete a single interaction
    elif request.method == 'DELETE':
        interaction = Interaction.objects.filter(id=pk).first()
        interaction.delete()
        return Response({'message': 'Interaction deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def publication_detail_api_view(request, pk=None):
    
    # Get a single publication
    if request.method == 'GET':
        publication = Publication.objects.filter(id=pk).first()
        publication_serializer = PublicationSerializer(publication)
        return Response(publication_serializer.data)
    
    # Update a single publication completely
    elif request.method == 'PUT':
        publication = Publication.objects.filter(id=pk).first()
        publication_serializer = PublicationSerializer(publication, data=request.data)
        if publication_serializer.is_valid():
            publication_serializer.save()
            return Response(publication_serializer.data)
        return Response(publication_serializer.errors)
    
    # Update a single publication partially
    elif request.method == 'PATCH':
        publication = Publication.objects.filter(id=pk).first()
        publication_serializer = PublicationSerializer(publication, data=request.data, partial=True)
        if publication_serializer.is_valid():
            publication_serializer.save()
            return Response(publication_serializer.data)
        return Response(publication_serializer.errors)

    # Delete a single publication
    elif request.method == 'DELETE':
        publication = Publication.objects.filter(id=pk).first()
        publication.delete()
        return Response({'message': 'Publication deleted successfully!'})


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
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def publication_type_detail_api_view(request, pk=None):
    
    # Get a single publication type
    if request.method == 'GET':
        publication_type = PublicationType.objects.filter(id=pk).first()
        publication_type_serializer = PublicationTypeSerializer(publication_type)
        return Response(publication_type_serializer.data)
    
    # Update a single publication type completely
    elif request.method == 'PUT':
        publication_type = PublicationType.objects.filter(id=pk).first()
        publication_type_serializer = PublicationTypeSerializer(publication_type, data=request.data)
        if publication_type_serializer.is_valid():
            publication_type_serializer.save()
            return Response(publication_type_serializer.data)
        return Response(publication_type_serializer.errors)
    
    # Update a single publication type partially
    elif request.method == 'PATCH':
        publication_type = PublicationType.objects.filter(id=pk).first()
        publication_type_serializer = PublicationTypeSerializer(publication_type, data=request.data, partial=True)
        if publication_type_serializer.is_valid():
            publication_type_serializer.save()
            return Response(publication_type_serializer.data)
        return Response(publication_type_serializer.errors)
    
    # Delete a single publication type
    elif request.method == 'DELETE':
        publication_type = PublicationType.objects.filter(id=pk).first()
        publication_type.delete()
        return Response({'message': 'Publication type deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def repetition_detail_api_view(request, pk=None):
    
    # Get a single repetition
    if request.method == 'GET':
        repetition = Repetition.objects.filter(id=pk).first()
        repetition_serializer = RepetitionSerializer(repetition)
        return Response(repetition_serializer.data)
    
    # Update a single repetition completely
    elif request.method == 'PUT':
        repetition = Repetition.objects.filter(id=pk).first()
        repetition_serializer = RepetitionSerializer(repetition, data=request.data)
        if repetition_serializer.is_valid():
            repetition_serializer.save()
            return Response(repetition_serializer.data)
        return Response(repetition_serializer.errors)
    
    # Update a single repetition partially
    elif request.method == 'PATCH':
        repetition = Repetition.objects.filter(id=pk).first()
        repetition_serializer = RepetitionSerializer(repetition, data=request.data, partial=True)
        if repetition_serializer.is_valid():
            repetition_serializer.save()
            return Response(repetition_serializer.data)
        return Response(repetition_serializer.errors)
    
    # Delete a single repetition
    elif request.method == 'DELETE':
        repetition = Repetition.objects.filter(id=pk).first()
        repetition.delete()
        return Response({'message': 'Repetition deleted successfully!'})


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

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail_api_view(request, pk=None):
    
    # Get a single user
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    
    # Update a single user completely
    elif request.method == 'PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
    # Update a single user partially
    elif request.method == 'PATCH':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
    # Delete a single user
    elif request.method == 'DELETE':
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response({'message': 'User deleted successfully!'})
