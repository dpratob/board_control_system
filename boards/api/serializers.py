from rest_framework import serializers
from boards.models import Board, BoardFeature, BoardPublication

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
