from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from users.models import User


def register(request):
    """Register new user"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return HttpResponse("Password must match confirmation")

        # Check if team member
        is_staff = False
        if "is_staff" in request.POST and request.POST["is_staff"]:
            is_staff = True

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)
            return HttpResponse('User created successfully')
        except IntegrityError:
            return HttpResponse("Username already taken")
    else:
        return HttpResponse('Method not allowed')


def login_view(request):
    """Login user"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            return HttpResponse('Incorrect credentials')


def logout_view(request):
    """Logout user"""
    logout(request)
    return HttpResponse('Logout successful')
