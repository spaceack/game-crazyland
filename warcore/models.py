from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from crazyland.settings import MEDIA_URL


# Create your models here.


# User表
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 与User是1对1关系
    org = models.CharField('Organization', max_length=128, blank=True)  # 用户名
    telephone = models.CharField('Telephone', max_length=50, blank=True)  # 电话
    avatar = models.BigIntegerField(null=True)
    static = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)  # 最后修改日期。系统自动生成
    class Meta:
        verbose_name = '用户'
    def __str__(self):
        return self.user.__str__()

# World 表
class World(models.Model):
    id = models.BigAutoField(primary_key=True)
    world_name = models.CharField(max_length=50, unique=True)
    init_gold = models.IntegerField('初始资金', default=999999)
    class Meta:
        verbose_name = '世界表'

# 地图表
class WorldMap(models.Model):
    base_id = models.BigIntegerField()
    type = models.CharField(max_length=16)

# App表
class App(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    nickname = models.CharField(max_length=50, unique=True)
    ip = models.IntegerField(null=True)
    static = models.IntegerField(default=1)
    world_id = models.IntegerField()

# 基地表
class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_id = models.BigIntegerField()
    basename = models.CharField(max_length=50, default='新基地')

# 事件表
class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()    # build, attack
    base_id = models.IntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    static = models.IntegerField()

# message
class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_id = models.BigIntegerField()
    to_id = models.BigIntegerField()
    content = models.TextField()
    create_at = models.TextField()

# object
class Object(models.Model):
    id = models.BigAutoField(primary_key=True)
    base_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1024)
    level = models.IntegerField()
    number = models.BigIntegerField()
    type = models.IntegerField()

# 兵种表
class Arms(models.Model):

    SX_CHOICE = (
        ('zs','战士'),
        ('tank','战车'),
        ('zc','战船'),
        ('zj','战机'),
        ('gs','工事'),
        ('kj','科技'),
        ('jz','建筑'),
    )

    name            = models.CharField('名称', max_length=64)
    img             = models.ImageField('图像', upload_to='image', null=True)
    desc            = models.CharField('简介', max_length=256)
    sx              = models.CharField('兵种属性', choices=SX_CHOICE, max_length=8)
    life            = models.IntegerField('生命', max_length=32, default=1)
    infantry_attack = models.IntegerField('对步兵攻击', default=0)
    tank_attack     = models.IntegerField('对战车攻击',default=0)
    air_attack      = models.IntegerField('对空军攻击',default=0)
    sea_attack      = models.IntegerField('对海军攻击',default=0)
    build_attack    = models.IntegerField('对工事攻击',default=0)
    build_limit     = models.IntegerField('建筑限制',default=0)
    kj              = models.IntegerField('科技限制', default=0)
    defense         = models.IntegerField('防御',default=0)
    price           = models.IntegerField('造价', default=99999)
    time            = models.IntegerField('建造时长(秒)',default=1)


    def img_id(self):
        return mark_safe('<img src="%s%s" width="100" height="100"/>' % (MEDIA_URL, self.img))

# news
class News(models.Model):
    TYPE_CHOICE = (
        ('kf', '开发日志'),
        ('jq', '军情播报'),
        ('gl', '游戏攻略'),
        ('fqa', '问题指南'),
    )
    title = models.CharField('标题', max_length=64)
    type = models.CharField('类型', choices=TYPE_CHOICE,max_length=8)
    content = models.TextField('正文')
    status = models.IntegerField('状态', default=1)
    crate_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name = '新闻'

    def __str__(self):
        return self.title