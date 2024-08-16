from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from users.views import RegisterView, ProfileView, email_verification, ResetPasswordView, UserDoesNotFound, \
    UserListView, UserUpdateView, UserViewSet, PaymentListAPIView, PaymentCreateAPIView, PaymentDestroyAPIView, \
    PaymentUpdateAPIView, PaymentRetriveAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
                  path('', LoginView.as_view(extra_context={'title': 'Вход'}, template_name='users/login.html'),
                       name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('profile/', ProfileView.as_view(), name='profile'),
                  path('email-confirm/<str:code>/', email_verification, name='email-confirm'),
                  path('pass_reset/', ResetPasswordView.as_view(), name='pass_reset'),
                  path('user_does_not_found/', UserDoesNotFound.as_view(), name='user_does_not_found'),
                  path("users_list/", UserListView.as_view(), name="users_list"),
                  path("update_user/<int:pk>/", UserUpdateView.as_view(), name="update_user"),

                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
                  path('payment/<int:pk>/', PaymentRetriveAPIView.as_view(), name='payment-get'),
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
                  path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment-delete'),

              ] + router.urls
