from django.urls import path

from accounts.views import AuthView, SignInView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
