
一个使用Django框架编写的策略类网络游戏项目

流程图

注册

登录


pip-compile --index-url=http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com requrements.in
pip install -r requrements.txt --index-url=http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com 

python manage.py makemigrations
python manage.py migrate