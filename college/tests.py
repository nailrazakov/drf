from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from college.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@sky.pro')
        self.course = Course.objects.create(name='Django', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        url = reverse("api:lesson_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_retrieve(self):
        url = reverse("api:lesson_retrieve", args=(self.lesson.pk, ))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            data.get("name"),
            self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("api:lesson_create")
        data = {
            "name": "JavaScript"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):
        url = reverse("api:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "JavaScript"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"),
            "JavaScript"
        )

    def test_lesson_delete(self):
        url = reverse("api:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )

    def test_subscribtion(self):
        url = reverse("api:subscriptions")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.all().count(),
            1
        )
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.all().count(),
            0
        )
