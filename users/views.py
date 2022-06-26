from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import User


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
                request, "users/register.html",
                {"form": CustomUserCreationForm}
                )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def update_profile(request):
    if request.method == "GET":
        return render(request, "users/profile.html",
                {"profile_form": ProfileForm, "user_form": CustomUserCreationForm}
            )
    elif request.method == "POST":
        r = request.POST
        with transaction.atomic():
            user = User.objects.get(pk=request.user.pk)
            if r.get("first_name", False):
                user.first_name = r["first_name"]
            if r.get("last_name", False):
                user.last_name = r["last_name"]
            if r.get("username", False):
                user.username = r["username"]
            if r.get("email", False):
                user.email = r["email"]
            if r.get("bio", False) or \
               r.get("location", False) or \
               r.get("birth_date", False):
                user = User.objects.get(pk=request.user.id)
                if r.get("bio", False):
                    user.profile.bio = r["bio"]
                if r.get("location", False):
                    user.profile.location = r["location"]
                if r.get("birth_date", False):
                    print(r["birth_date"])
                    user.profile.birth_date = r["birth_date"]

            user.save()
        return redirect(reverse("dashboard"))
