from django.shortcuts import render, redirect
from .models import user_info
from .forms import Userinfo_Form

def add_user(request):

    if request.method == 'POST':
        form = Userinfo_Form(request.POST)
        if form.is_valid():
            print(form)
            print('form')
            form.save()
            return redirect('login')  # Redirect to the login
        else:
            print(form.errors)
    else:
        form = Userinfo_Form()

    context = {
        'form' : form ,
    }

    return render(request, 'user/add_user.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username', 'null')
        print(username)
        print('username')
        password = request.POST.get('password', 'null')
        print(password)
        print('password')
        email = request.POST.get('email', 'null')
        print(email)
        print('email')


        user_object = user_info.objects.none()
        if user_info.objects.filter(name = username).exists():
            user_object = user_info.objects.get(name = username)
            if user_object.password == password and user_object.email == email :
                return redirect ('tasks', user_object.name)
        else:
            return redirect('landing')  # Redirect to the landing page



    else:
        form = Userinfo_Form()

    context = {
        'form' : form ,
    }

    return render(request, 'user/login.html', context)
