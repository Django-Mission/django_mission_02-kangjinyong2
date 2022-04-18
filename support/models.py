from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from distutils.command.sdist import sdist
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Faq(models.Model):
    C_CHOICES = (
        ('general','일반'),
        ('account','계정'),
        ('etc','기타'),
    )
    category = models.CharField(verbose_name='카테고리',max_length=8,choices=C_CHOICES,null=True)# 카테고리
    author = models.ForeignKey(User,verbose_name='작성자',on_delete=models.CASCADE,null=True)
    subject=models.CharField(verbose_name='제목',null=True,default='',max_length=200) # 문자최대길이
    content=models.TextField(verbose_name='내용') # 글자수 제한없음
    create_date=models.DateTimeField(verbose_name='작성일',auto_now_add = True) # 생성시간
    updated_at = models.DateTimeField(verbose_name='최종수정일',auto_now = True,null=True,blank=True) # 수정시간
    #writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    #modify_date=models.DateTimeField(null=True,blank=True)
    #voter=models.ManyToManyField(User,related_name='voter_Question')
    def _str_(self):
        return self.subject
    
class Answer(models.Model):
    C_CHOICES = (
        ('general','일반'),
        ('account','계정'),
        ('etc','기타'),
    )
    category = models.CharField(verbose_name='카테고리',max_length=8,choices=C_CHOICES,null=True)
    author = models.ForeignKey(User,verbose_name='작성자',on_delete=models.CASCADE)
    question=models.ForeignKey(Faq,on_delete=models.CASCADE)
    content=models.TextField(verbose_name='내용')
    create_date=models.DateTimeField(verbose_name='작성일',auto_now = True)
    updated_at = models.DateTimeField(verbose_name='최종수정일',auto_now = True) # 수정시간
    #modify_date=models.DateTimeField(null=True,blank=True)
    #voter=models.ManyToManyField(User,related_name='voter_Answer')
# class Faq(models.Model):
#     C_CHOICES = (
#         ('general','일반'),
#         ('account','계정'),
#         ('etc','기타'),
#     )
#     category = models.CharField(verbose_name='카테고리',max_length=8,choices=C_CHOICES,null=True)
#     author=models.ForeignKey(User,verbose_name='작성자',on_delete=models.CASCADE)
#     content=models.TextField(verbose_name='내용')
#     create_date=models.DateTimeField(verbose_name='작성일',auto_now = True) 
#     updated_at = models.DateTimeField(verbose_name='최종수정일',auto_now = True) # 수정시간
#     #modify_date=models.DateTimeField(null=True,blank=True)
#     question=models.ForeignKey(Question,verbose_name='질문',null=True,blank=True,on_delete=models.CASCADE)
#     answer=models.ForeignKey(Answer,verbose_name='답변',null=True,blank=True,on_delete=models.CASCADE)
    
