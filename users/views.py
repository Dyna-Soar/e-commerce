from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError

from users.models import User


class UserManagement:
    def register(self, request):
        """Register new user"""
        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]

            # Ensure password matches confirmation
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]

            if password != confirmation:
                return "Password must match confirmation", 406

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return 'User created successfully', 200
            except IntegrityError:
                return "Username already taken", 403
        else:
            return 'Method not allowed', 405


class UserAuthentication:
    def login_view(self, request):
        """Login user"""
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return 'Login successful', 200
            else:
                return 'Incorrect credentials', 406

    def logout_view(self, request):
        """Logout user"""
        logout(request)
        return 'Logout successful', 204

