from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from college.models import Course, Lesson
from users.models import User, Payments


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
