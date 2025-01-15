from rest_framework import serializers
from boards.models import Board, BoardFeature

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardFeature
        fields = '__all__'