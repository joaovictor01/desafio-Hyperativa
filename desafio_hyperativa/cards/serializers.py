from rest_framework import serializers
from .models import Card, CardsBatch


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "name", "card_number"]


class GetCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id"]


class CardsBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardsBatch
        fields = ["id", "file"]
