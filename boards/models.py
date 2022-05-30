from statistics import mode
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models

# from users.models import User
from django.utils.translation import gettext_lazy as _

class Content(models.Model):

    class ContentTypes(models.TextChoices):
        Free = 'Free', _('Free')
        Information = 'Info', _('Info')

    content_id = models.AutoField(primary_key=True, unique=True, null=False)
    ananymous = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)
    content_class = models.CharField(max_length = 30, choices=ContentTypes.choices, default=ContentTypes.Free)
    title = models.CharField(max_length=100, null = False)
    content = models.CharField(max_length=255, )

    #user_name = models.ForeignKey("users.User", on_delete = models.CASCADE)
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, unique=True, null=False)
    commnent = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)
    depth = models.IntegerField(null=False)
    has_repo = models.BooleanField(null=False)

    user_name =  models.ForeignKey("users.User", on_delete = models.CASCADE)
    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey('self', on_delete=models.CASCADE)


class React(models.Model):
    
    class ReactChoice(models.TextChoices):
        good = 'GOOD', _('GOOD')
        bad = 'BAD', _('BAD')
    
    react_id = models.AutoField(primary_key=True, unique=True, null=False)
    react_type = models.CharField(max_length=30, choices=ReactChoice.choices, null=False, default=ReactChoice.good)

    user_name =  models.ForeignKey("users.User", on_delete = models.CASCADE)
    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Detach(models.Model):
    detach_id = models.AutoField(primary_key=True, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add = True, null = False)
    updated_at = models.DateTimeField(auto_now_add = True, null = False)

    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

    ## 이미지를 배열 형태로 생성할 지 데이터 모델을 쓸 지 고민 중...
    ## 현 상황에서 이미지는 넣지 않는 것으로 간주 한다. 



class Image(models.Model):
    ## 이미지 파일 관리 어떻게 할지? 서버를 따로 쓴다면 어떻게? 여러 서버 간 어떻게??
    image_id = models.AutoField(primary_key=True, unique=True, null=False)
    path = models.ImageField(upload_to='images/detach/')

    detach_id = models.ForeignKey(Detach, on_delete=models.CASCADE, null=True) 
    content_id  = models.ForeignKey(Content, on_delete = models.CASCADE, null=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    
class File(models.Model):
    ## 파일 관리 어떻게 할지? 서버를 따로 쓴다면 어떻게? 여러 서버 간 어떻게??
    ## 파일 .exe 파일 같은 거 안되게 해야 함. 
    ## 여기에는 확장자로 관리하지만 보안 문제가 있을 수도 있기에 
    ## https://lynlab.co.kr/blog/60 mime 파일 같은 거 사용하기로 한다.(근데 이것도 unix인지 아닌 지 에 땨라 의존성이 존재)
    ## 지금 현재 보안은 신경쓰지 않기로 한다. 

    image_id = models.AutoField(primary_key=True, unique=True, null=False)
    path = models.ImageField(upload_to='media/file')

    detach_id = models.ForeignKey(Detach, on_delete=models.CASCADE, null=True) 