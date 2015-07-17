from rest_framework import serializers
from .models import UserVideoMetric


class UserVideoMetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserVideoMetric
