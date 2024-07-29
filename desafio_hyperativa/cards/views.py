import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .models import Card, CardsBatch
from .serializers import CardSerializer, GetCardSerializer, CardsBatchSerializer
from rest_framework.permissions import IsAuthenticated
from .tasks import process_cards_batch

logger = logging.getLogger("desafio_hyperativa")


class CardCreateView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        card = serializer.save()
        logger.info(
            f"Card created: {card.name} with ID {card.id} and number {card.card_number}"
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CardsBatchCreateView(generics.CreateAPIView):
    queryset = CardsBatch.objects.all()
    serializer_class = CardsBatchSerializer
    parser_classes = [FileUploadParser]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        batch = serializer.save()
        process_cards_batch.delay(batch.id)
        logger.info(f"CardsBatch created with ID {batch.id}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CardRetrieveByNumberView(generics.RetrieveAPIView):
    serializer_class = GetCardSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        card_number = self.kwargs["card_number"]
        card = Card.objects.get(card_number=card_number)
        logger.info(f"Card retrieved: {card.name} with ID {card.id}")
        return card
