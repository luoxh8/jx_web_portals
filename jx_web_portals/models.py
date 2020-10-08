from django.db.models import *


class BaseModel(Model):
    created_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = BooleanField(default=False, verbose_name='是否删除')

    class Meta: abstract = True
