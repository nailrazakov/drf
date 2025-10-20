from django.contrib import admin

from college.models import Course, Lesson
from users.models import User
from users.services import  Payments

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Payments)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
