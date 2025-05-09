from .models import *
from rest_framework import serializers


class UserFSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='users')

    class Meta:
        model = UserF
        fields = ['id', 'url', 'username', 'email', 'email_confirmed']


class UserFNestedSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserF
        fields = ['id', 'username']


class StatementSerializer(serializers.HyperlinkedModelSerializer):
    author = UserFNestedSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='statements')

    class Meta:
        model = Statement
        fields = ['id', 'url', 'author', 'category', 'title', 'text', 'attachments', 'created_at']

class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserFNestedSerializer(read_only=True)
    statement = StatementSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='reactions')

    class Meta:
        model = Reaction
        fields = ['id', 'url', 'author', 'statement', 'text', 'created_at', 'is_accepted']