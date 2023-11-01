from django.urls import path
from rest_framework.routers import DefaultRouter

from payment.apps import PaymentConfig
from payment.views import  PaymentListAPIView, GetPaymentView, PaymentCreateAPIView

app_name = PaymentConfig.name

router = DefaultRouter()


urlpatterns = [
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/<str:payment_id>/', GetPaymentView.as_view(), name='payment_get'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
] + router.urls