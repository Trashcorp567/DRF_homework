from rest_framework import serializers
from stripe.api_resources.payment_intent import PaymentIntent

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    pay = PaymentIntent.stripe_id
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Payment
        fields = '__all__'