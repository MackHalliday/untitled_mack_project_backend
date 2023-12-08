from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        messages.success(request, "Your account has been created.")

        return redirect("signin")

    return render(request, "authentication/signup.html")


def signin(request):
    return render(request, "authentication/signin.html")


def signout(request):
    pass
