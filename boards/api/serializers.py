from rest_framework import serializers
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
