from django.urls import path

from accounts.api.v1.views import LoginAPIView, SignUpAPIView

app_name = 'account-api-v1'
urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('register/', SignUpAPIView.as_view(), name='user-register'),
]
