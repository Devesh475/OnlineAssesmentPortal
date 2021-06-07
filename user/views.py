from .models import userprofile
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import createUser
from django.contrib.auth import login, logout
from assesment.models import questionPaper, question
# Create your views here.

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            lst = []
            for x in userprofile.objects.all():
                lst.append(x.user)
            if user not in lst:
                userP = userprofile.objects.create(user=user)
                userP.status = True
                userP.save()
            return redirect('/')
    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)

def logoutpage(request):
    logout(request)
    return redirect('/')

def register(request):
    form = createUser(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "User Created Successfully")
        return redirect('login')
    template_name = "createuser.html"
    context = {"form":form}
    return render(request, template_name, context)