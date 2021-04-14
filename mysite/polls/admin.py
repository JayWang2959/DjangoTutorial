from django.contrib import admin
from .models import Question

# 向管理页面注册Question类
admin.site.register(Question)

