from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .serializers import BetSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from bet.models import Bet
from bet.calculate_bet import parse_db


class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    queryset=Bet.objects.all()

    @action(methods=['get'], detail=False)
    def calculate(self, obj):
        parse_db()
        return HttpResponse(status=status.HTTP_200_OK)
