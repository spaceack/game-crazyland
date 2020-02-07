import logging
from django.shortcuts import render, HttpResponse
from .models import User, App, Base, UserProfile, News
from django.contrib import auth
from warcore.forms import LoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def index(request):
    l = News.objects.all()
    print(l)
    return render(request, 'index.html', {"news":l})

def world(request):
    return render(request, 'world.html', {})

def register(request):
    '帐号注册'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            return render(request, 'registration.html', {'form': form, 'message': '注册成功, 请登录', 'code': 1})
        else:
            # 注册失败
            return render(request, 'registration.html', {'form': form, 'message': '注册失败', 'code': 0})


    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def login(request):
    '帐号登录'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('index')

            else:
                # 登陆失败
                return render(request, 'login.html', {'form': form, 'message': '密码错误，请再次尝试'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect("index")


def regist(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username','')
            password = request.POST.get('password', '')
            email = request.POST.get('email','')
            mobile = request.POST.get('avatar','')
            nickname = request.POST.get('nickname','')
            world_id = request.POST.get('world_id','')
            user = User(username=username, password=password, email=email, mobile=mobile)
            user.save()

            app = App(nickname=nickname, user_id=user.id, world_id=world_id)
            app.save()

            base =  Base(app_id=app.id)
            base.save()

            return HttpResponse({'code':0, 'message':'注册成功'})
    except Exception as e:
        logger.warning(e)
        return HttpResponse({'code': 1, 'message': '注册失败'})

def user_all_base(request):
    try:
        if request.method == 'GET':
            app_id = request.GET.get('app_id','')
            base_list = Base.objects.filter(app_id=app_id)
            return HttpResponse({'code':0, 'message':'成功', 'data': base_list})
    except Exception as e:
        logger.warning(e)
        return HttpResponse({'code': 1, 'message': '失败'})