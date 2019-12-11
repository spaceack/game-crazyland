from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# User表
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=16, null=True)
    avatar = models.BigIntegerField(null=True)
    static = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)

# World 表
class World(models.Model):
    id = models.BigAutoField(primary_key=True)
    world_name = models.CharField(max_length=50, unique=True)


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