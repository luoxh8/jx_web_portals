from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from jx_web_portals.models import *


class News(BaseModel):
    author = ForeignKey(User, CASCADE, verbose_name='作者')
    content = RichTextField(verbose_name='新闻内容')
