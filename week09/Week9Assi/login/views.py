from django.shortcuts import render
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                return HttpResponse('登陆失败,用户名或密码错误.')
        else:
            return HttpResponse('请输入姓名和密码.')

    if request.method =='GET':
        login_form = LoginForm()
        return render(request, 'loginform.html', {'form': login_form})

