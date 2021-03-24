from .models import Law
from rest_framework import serializers


class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'title', 'content']
