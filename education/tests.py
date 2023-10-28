from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase

from config import settings
from education.models import Course, Lesson, Subscription, Payment
from education.validators import LinkValidator
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_course(self):
        data = {
            "name": 'Тест курс',
            "description": 'Тест описание'
        }
        response = self.client.post(
            '/course/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'subscription': 'Подписка отсутствует', 'lesson': [], 'number_of_lessons': 0, 'name': 'Тест курс',
             'image': None, 'description': 'Тест описание', 'owner': None}

        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_list_course(self):

        Course.objects.create(
            name='Тест курс',
            description='Тест описание'
        )

        response = self.client.get(
            '/course/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json()['results'],
            [{'id': 2, 'subscription': 'Подписка отсутствует', 'lesson': [], 'number_of_lessons': 0,
              'name': 'Тест курс', 'image': None, 'description': 'Тест описание', 'owner': None}]
        )


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        data = {
            'name': 'Тест урок',
            'description': 'Тест описание'
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_view_lesson_list(self):
        response = self.client.get(
            '/lesson/',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        lesson = Lesson.objects.create(
            name='Тест урок',
            description='Тест описание'
        )
        data = {
            'name': 'Тест урок2',
            'description': 'Тест описание2'
        }
        response = self.client.patch(
            f'/lesson/update/{lesson.id}/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        lesson = Lesson.objects.create(
            name='Тест урок',
            description='Тест описание'
        )
        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class PaymentTestCase(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.user = User.objects.create(email='admin@gmail.com', password='testpassword')
        self.course = Course.objects.create(name='Test Course', owner=self.user)
        self.payment_data = {
            'user': self.user.id,
            'paid_course': self.course.id,
            'paid_cost': 100,
            'pay_method': 'cash'
        }

    def test_create_payment(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/payment/create/',
            data=self.payment_data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        """Проверка, что после создания оплаты, статус подписки принял значение True"""
        subscription = Subscription.objects.get(user=self.user, course=self.course)
        self.assertTrue(
            subscription.active_sub
        )
