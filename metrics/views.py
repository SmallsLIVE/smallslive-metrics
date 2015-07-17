from rest_framework import generics
from .models import UserVideoMetric
from .serializers import UserVideoMetricSerializer


class MetricView(generics.CreateAPIView):
    model = UserVideoMetric
    serializer_class = UserVideoMetricSerializer

metric_view = MetricView.as_view()
