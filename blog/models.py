import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from .validators import MinLengthValidator, lnglat_validator, ZipCodeValidator
from .fields import PhoneNumberField

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
            validators=[MinLengthValidator(4), ZipCodeValidator(True)],
            verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
            validators=[MinLengthValidator(10)])
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message= models.TextField()

class Tag(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name= models.CharField(max_length=20)
    phone_number = PhoneNumberField()

class ZipCode(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    code = models.CharField(max_length=7)

    def __str__(self):
            return self.name



# Create your models here.
#class PhoneNumberField(models.CharField):
#    def __init__(self, *args)
#def phone_number_validator(value):
#    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
#        raise ValidationError('휴대폰 번호를 입력해주세요.')
