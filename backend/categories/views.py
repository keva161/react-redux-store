from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer
from datetime import datetime, timezone, timedelta

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer