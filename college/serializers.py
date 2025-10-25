from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from college.models import Course, Lesson, Subscription
from college.validators import validate_url


class LessonSerializer(serializers.ModelSerializer):
    url_video = serializers.CharField(validators=[validate_url], required=False)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    signed = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_signed(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user, course=course).exists()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
