from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
import stripe
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


# Create your views here.
class PaymentCreateAPIView(generics.CreateAPIView):
    '''Создания платежа'''
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe.api_key = "sk_test_51O7I7xCSnsbuF4sTZ0xNaOWOE3R7OESs6WnHeVwWG5RUdA30OJRRVjZisSWTAH4PHEffX065dVIwgHxGgg5zbD0y00up2ozLiZ"
        pay = stripe.PaymentIntent.create(
            amount=payment.paid_cost,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()
        return super().perform_create(serializer)


class PaymentListAPIView(generics.ListAPIView):
    '''Просмотр списка платежей'''
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'pay_method')
    ordering_fields = ('payment_date',)


class GetPaymentView(APIView):
    '''Просмотр платежа по его id'''
    def get(self, request, payment_id):
        stripe.api_key = "sk_test_51O7I7xCSnsbuF4sTZ0xNaOWOE3R7OESs6WnHeVwWG5RUdA30OJRRVjZisSWTAH4PHEffX065dVIwgHxGgg5zbD0y00up2ozLiZ"
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        print(payment_intent)
        return (Response
            ({
            'status': payment_intent.status,
            'body': payment_intent}))


