from django.shortcuts import render
from django.views import View
from .forms import Login,Profile
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import CustomUser



class UserLoginView(View):
    def get(self, request):
        form = Login()  # ❗️ signup form emas
        return render(request, "pages/login.html", {"form": form})

    def post(self, request):
        form = Login(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Login yoki parol noto‘g‘ri!")
        
        return render(request, "pages/login.html", {"form": form})


def profile_view(request):
    user = request.user

    if request.method == 'PUT':
        profile = Profile(request.FORM)
        if profile.is_valid():
            profile
    return render(request,'pages/profile.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')