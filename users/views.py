from rest_framework.generics import ListAPIView
from users.models import Payments
from users.serializers import PaymentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PaymentListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['date']
