from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


class UserFViewset(viewsets.ModelViewSet):
   queryset = UserF.objects.all()
   serializer_class = UserFSerializer


class StatementViewset(viewsets.ModelViewSet):
   queryset = Statement.objects.all()
   serializer_class = StatementSerializer


class ReactionViewset(viewsets.ModelViewSet):
   queryset = Reaction.objects.all()
   serializer_class = ReactionSerializer