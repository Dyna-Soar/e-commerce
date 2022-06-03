from django.contrib.auth import authenticate, login, logout

from users.models import User


class UserManagement:
    def create_user(self, request):
        if request.method == "POST":
            data = request.POST
            try:
                user = User.objects.create(
                    username=data["username"],
                    password=data["password"],
                    email=data["email"]
                )
                user.save()
                return 'User created successfully', 200
            except AssertionError:
                return 'Unable to create user', 406
        else:
            return 'Method not allowed', 405


class UserAuthentication:
    def login_view(self, request):
        if request.method == "POST":
            data = request.POST
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return 'Login successful', 200
            else:
                return 'Incorrect credentials', 406

    def logout_view(self, request):
        logout(request)
        return 'Login successful', 204

