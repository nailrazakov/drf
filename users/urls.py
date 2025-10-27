from django.urls import path
from users.views import (PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView,
                         UserDestroyAPIView, PaymentCreateView)
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delete'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

