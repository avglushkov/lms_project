from rest_framework import serializers
from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, source='payment_set')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'town', 'payments')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
