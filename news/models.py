from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from jx_web_portals.models import *


class NewsModel(BaseModel):
    author = ForeignKey(User, CASCADE, verbose_name='作者')
    content = RichTextField(verbose_name='新闻内容')

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}...'

    class Meta:
        verbose_name = '新闻管理'
        verbose_name_plural = '新闻管理'
