import logging
from django.shortcuts import render, HttpResponse
from .models import User, App, Base

# Create your views here.
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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