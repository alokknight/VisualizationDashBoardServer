from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from .models import DataPoint
from .serializers import DataPointSerializer
from django_filters import rest_framework as filters
from .filters import DataPointFilter


class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

class DataPointFilterViewSet(viewsets.ModelViewSet):
    serializer_class = DataPointSerializer
    queryset = DataPoint.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DataPointFilter