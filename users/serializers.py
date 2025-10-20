from rest_framework.serializers import ModelSerializer
from users.models import User
from users.services import Payments


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(source='user_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserPublicSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'first_name']
