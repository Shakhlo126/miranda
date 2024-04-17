from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import (Category,
                     Politics,
                     Health,
                     Sport,
                     Design,
                     Business)

from .serializers import (CategorySerializer,
                          PoliticsSerializer,
                          HealthSerializer,
                          SportSerializer,
                          DesignSerializer,
                          BusinessSerializer)

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PoliticsAPIView(generics.ListAPIView):
    queryset = Politics.objects.all()
    serializer_class = PoliticsSerializer

class HealthAPIView(generics.ListAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer

class SportAPIView(generics.ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class DesignAPIView(generics.ListAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

class BusinessAPIView(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class HomeAPIView(generics.ListAPIView):
    queryset = Category.objects.all()[:9]
    serializer_class = CategorySerializer


