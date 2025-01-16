from rest_framework import serializers
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, Interaction, Publication, PublicationType, Repetition, User

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardFeature
        fields = '__all__'

class BoardPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardPublication
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class PublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationType
        fields = '__all__'

class RepetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repetition
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
