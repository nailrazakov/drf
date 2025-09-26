from django.urls import path
from rest_framework.routers import SimpleRouter
from college.views import (CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView,
                           LessonUpdateAPIView, LessonDestroyAPIView)
from college.apps import CollegeConfig

app_name = CollegeConfig.name

router = SimpleRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
]
urlpatterns += router.urls
