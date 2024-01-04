from django.db import models

# Create your models here.

# 在企业中：
#    1. 开会讨论立项，一般由产品经理主导.
#    2. 需求分析：功能需求
#    3. 设计数据库：先写models

class UserModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()  # 非负数


# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate



