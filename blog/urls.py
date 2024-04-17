from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('sport/', SportAPIView.as_view(), name='sport'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('health/', HealthAPIView.as_view(), name='health'),
    path('business/', BusinessAPIView.as_view(), name='business'),
    path('design/', DesignAPIView.as_view(), name='design'),
    path('politics/', PoliticsAPIView.as_view(), name='politics'),
]