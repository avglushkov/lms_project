from rest_framework import serializers
from users.models import User, Payment
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, source='payment_set')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'town', 'payments')

