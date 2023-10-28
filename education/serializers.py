from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from education.models import Course, Lesson, Payment, Subscription


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.paid_course:
            course_data = CourseSerializer(instance.paid_course).data
            data['course'] = course_data
        elif instance.paid_lesson:
            lesson_data = LessonSerializer(instance.paid_lesson).data
            data['lesson'] = lesson_data

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        payment = super().create(validated_data)

        if payment.paid_course:
            course = payment.paid_course
        elif payment.paid_lesson:
            course = payment.paid_lesson.course

        subscription, created = Subscription.objects.get_or_create(user=user, course=course)
        subscription.active_sub = True
        subscription.save()

        return payment


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    number_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_subscription(self, value):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            is_subscribed = Subscription.objects.filter(course=value, user=user, active_sub=True).exists()
            if is_subscribed:
                return 'Подписка активна'
        return 'Подписка отсутствует'

    def get_number_of_lessons(self, instance):
        return instance.lesson_set.count()
