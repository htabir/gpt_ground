from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import User


class AuthView(View):
    def get(self, request):
        return render(request, 'accounts/auth.html')


class SignInView(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            return render(request, 'accounts/auth.html', {'error': 'Invalid email/password'})

        user = User.objects.get(email=email)
        if not user.check_password(password):
            return render(request, 'accounts/auth.html', {'error': 'Password is incorrect'})

        authenticate(request, email=email, password=password)

        return redirect('accounts:auth')


class SignUpView(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/auth.html', {'error': 'Email is taken'})

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=email,
            email=email,
            password=password,
        )

        authenticate(request, email=email, password=password)

        return redirect('accounts:auth')
