from django.shortcuts import render, HttpResponse
from One2Many.models import *

# 一对多关系

# 添加数据
def add_user(request):
    # 给UserType添加数据
    # user_types = ['青铜', '白银', '黄金', '钻石', '大师', '王者']
    # for name in user_types:
    #     UserType.objects.create(name=name)

    # 给User添加数据
    for i in range(11, 30):
        # User.objects.create(name=f'张三-{i}',age=i,
        #                     user_type_id=i%6 + 1)

        User.objects.create(name=f'李四-{i}', age=100+i,
                            user_type=UserType.objects.get(pk=i%6 + 1))

    return HttpResponse('添加成功!')


# 删除数据
def del_user(request):
    # 删除User数据
    # User.objects.filter(id=6).delete()

    # 删除UserType数据
    UserType.objects.filter(id=3).delete()

    return HttpResponse('删除成功!')


# 修改数据
def update_user(request):
    # 修改UserType
    # UserType.objects.filter(id=1).update(name='钻石')

    # 修改User
    User.objects.filter(id=2).update(age=1000)

    return HttpResponse('修改成功!')


# 查询数据
def get_user(request):

    # 正向查询：从User表去查找UserType
    # user = User.objects.get(id=2)
    # print(user.name, user.age, user.user_type, user.user_type_id)
    # print(user.user_type.name, user.user_type.id)  # User所属UserType的所有数据

    # 反向查询：
    # utype = UserType.objects.get(pk=1)
    # print(utype.id, utype.name)  # UserType自己的属性
    # user_set: 内部自动会生成的属性，可以让你反向查询到所有User集合
    # print(type(utype.user_set))  # RelatedManager 关联的管理器对象
    # <class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
    # print(utype.user_set.all())  # 查询集 QuerySet
    # print('-' * 60)

    # 在filter中还可以这么用
    # 比如:查找用户类型名称为’白银‘的所有用户
    # users = User.objects.filter(user_type=UserType.objects.get(name='白银'))  # 传入UserType对象
    # users = User.objects.filter(user_type_id=2)  # 传入user_type_id
    users = User.objects.filter(user_type__name='白银')  # 传入UserType对象的name属性作为条件
    print(users)
    print('-' * 60)

    # related_name：关联名称
    utype = UserType.objects.get(pk=1)
    # print(utype.user_set.all())  # 报错，使用了related_name就不可以在使用带_set的属性
    print(utype.users.all())

    return HttpResponse('查询成功!')


