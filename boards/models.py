from statistics import mode
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models

from . import User



class Content(models.Model):

    class ContentTypes(models.TextChoices):
        Free = 'Free', _('Free')
        Information = 'Info', _('Info')

    content_id = models.AutoField(primary_key=True, unique=True, null=False)
    ananymous = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)
    content_class = models.CharField(choices=ContentTypes, default=ContentTypes.Free)
    title = models.CharField(max_length=100, null = False)
    content = models.CharField(max_length=255, )

    user_name = models.ForeignKey(User, on_delete = models.CASCADE)
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, unique=True, null=False)
    commnent = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)
    depth = models.IntegerField(null=False)
    has_repo = models.BooleanField(null=False)

    user_name =  models.ForeignKey(User, on_delete = models.CASCADE)
    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey('self', on_delete=models.CASCADE)


class React(models.Model):
    
    class ReactChoice(models.TextChoices):
        good = 'GOOD', _('GOOD')
        bad = 'BAD', _('BAD')
    
    react_id = models.AutoField(primary_key=True, unique=True, null=False)
    react_type = models.CharField(choices=ReactChoice, null=False, default=ReactChoice.good)

    user_name =  models.ForeignKey(User, on_delete = models.CASCADE)
    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Detach(models.Model):
    detach_id = models.AutoField(primary_key=True, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)

    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

    ## 이미지를 배열 형태로 생성할 지 데이터 모델을 쓸 지 고민 중...
    


class Image(models.Model):
    image_id = models.AutoField(primary_key=True, unique=True, null=False)



    
class File(models.Model):
    pass