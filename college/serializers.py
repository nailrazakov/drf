from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from college.models import Course, Lesson
from college.validators import validate_url


class LessonSerializer(serializers.ModelSerializer):
    url_video = serializers.CharField(validators=[validate_url])
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Course
        fields = '__all__'
