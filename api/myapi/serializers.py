from .models import Law, DailyId
from rest_framework import serializers


class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'title', 'content']


class DailyIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyId
        fields = ['id']
