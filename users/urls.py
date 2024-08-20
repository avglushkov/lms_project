from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView, PaymentCreateAPIView, PaymentDestroyAPIView, \
    PaymentUpdateAPIView, PaymentRetriveAPIView, UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [

                  path('register/', UserCreateAPIView.as_view(), name='register'),

                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
                  path('payment/<int:pk>/', PaymentRetriveAPIView.as_view(), name='payment-get'),
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
                  path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment-delete'),

                  path('login/', TokenObtainPairView.as_view(permission_classes = [AllowAny]), name='login'),
                  path('token/refresh/', TokenRefreshView.as_view(permission_classes = [AllowAny]), name='token_refresh'),

              ] + router.urls
