from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.messages import success, error
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from .models import User

# Create your views here.
# def users_create(request):
#     if request.method == "GET":
#         form =  UserCreationForm()

#     else:
#         form = UserCreationForm(data=request.POST)

#         if form.is_valid():
#             form.save()
#             success(request, "Account created.")
#             return redirect(to='questions_list')

#     return render(request, "users/users_create.html", {"form": form})


# def users_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             success(request, "login succeeded.")
#             return redirect(to="questions_list")

#     return render(request, "users/users_login.html")


# @login_required
# def users_logout(request):
#     logout(request)
#     success(request, "logout succeeded.")
#     return redirect(to="users_login")