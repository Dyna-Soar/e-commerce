from django.http import HttpResponse
from django.db import IntegrityError
from clients.models import ClientUser, Card


def client_register(request):
    """Register new client"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        country = request.POST["country"]
        zip_code = request.POST["zip_code"]
        address = request.POST["address"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return HttpResponse("Password must match confirmation")

        # Attempt to create new user
        try:
            client_user = ClientUser.objects.create_user(username=username, email=email, password=password)
            return HttpResponse('Client created successfully')
        except IntegrityError:
            return HttpResponse("Username already taken")
    else:
        return HttpResponse('Method not allowed')
