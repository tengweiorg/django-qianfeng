import math

from django.db.models import Max, Min, Sum, Avg, Count
from django.shortcuts import render, HttpResponse

# 导入models
from App.models import *


# 增加数据
def add_person(request):
    # 方式1
    # try:
    #     p = PersonModel()
    #     p.name = '李四'
    #     p.age = 44
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式2
    # try:
    #     p = PersonModel(name='王五', age=55)
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式3
    # try:
    #     PersonModel.objects.create(name='赵六', age=66)
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式4
    # try:
    #     ret = PersonModel.objects.get_or_create(name='钱七', age=77)
    #     print('ret:', ret)
    #     # ret: (<PersonModel: PersonModel object (5)>, True)
    #     # 如果是第一次创建：则是True，如果已经存在则是False
    #
    # except Exception as e:
    #     return HttpResponse('添加失败')

    # 添加多条数据
    for i in range(21, 100):
        PersonModel.objects.create(name=f'武{i}范', age=i)

    return HttpResponse('添加成功!')


# 删除数据
def del_person(request):
    # 删除数据:
    #  1. 先找到要删除的数据
    #  2. 然后删除
    try:
        # 删除一条数据
        # p = PersonModel.objects.first()  # 第一条数据
        # p.delete()

        # 删除多条数据
        PersonModel.objects.filter(age__gt=15).delete()  # age>15的多条数据

    except Exception as e:
        return HttpResponse('删除失败!')

    return HttpResponse('删除成功!')


# 修改数据
def update_person(request):
    # 修改数据
    #  1. 先找到要修改的数据
    #  2. 然后修改
    try:
        # 修改一条数据
        p = PersonModel.objects.first()
        p.age = 666
        # p.save()  # 同步到数据库表中
        p.save(update_fields=['age'])  # 指定更新的字段，提高更新效率

        # 修改多条数据
        # PersonModel.objects.all().update(age=100)

    except Exception as e:
        return HttpResponse('修改失败！')

    return HttpResponse('修改成功！')


# 查询数据
def get_person(request):

    # get(): 得到一个对象(一条数据)
    #        如果没有找到符合条件的对象，会引发模型类.DoesNotExist异常
    # 	     如果找到多个，会引发模型类.MultipleObjectsReturned 异常
    p = PersonModel.objects.get(id=18)
    # p = PersonModel.objects.get(18)  # 不可以这样写，会报错
    p = PersonModel.objects.get(pk=18)  # pk:primary key
    p = PersonModel.objects.get(age=666)  # 可以
    # p = PersonModel.objects.get(age=100)  # 不可以，报错，MultipleObjectsReturned
    # p = PersonModel.objects.get(age=1000)  # 不可以，报错，DoesNotExist
    # print('*' * 60)
    # print(p, type(p))  # PersonModel对象
    # print(p.name, p.age)
    # print('*' * 60)

    # all(): 获取所有数据
    persons = PersonModel.objects.all()
    print(persons, type(persons))
    # QuerySet 查询集
    # 可以遍历查询集
    for p in persons:
        print(p.name, p.age)

    # first(): 第一条数据
    p = PersonModel.objects.first()
    print(p.name, p.age)

    # last(): 最后一条数据
    p = PersonModel.objects.last()
    print(p.name, p.age)

    # filter(): 过滤，使用最多
    persons = PersonModel.objects.filter()  # 默认没有条件，得到所有数据
    persons = PersonModel.objects.filter(age__gt=300)  # age>300
    persons = PersonModel.objects.filter(age__gte=300)  # age>=300
    persons = PersonModel.objects.filter(age__lt=300)  # age<300
    persons = PersonModel.objects.filter(age__lte=300)  # age<=300
    persons = PersonModel.objects.filter(age=300)  # age=300
    # 查询集可以做链式调用
    # print(persons.filter().filter().all().first())
    print(type(persons))  # django.db.models.query.QuerySet
    for p in persons:
        print('--- ', p.name, p.age)

    print(persons.first())
    print(persons.last())
    print(persons.exists())  # 查询集是否存在数据，如果存在则为True，否则为False
    print(persons.count())  # 查询集中的数据个数

    # values() 和 values_list()
    persons = PersonModel.objects.filter()
    print("persons:", persons)
    print("list(persons):", list(persons))  # 将查询集强制转换成列表
    # values() : 列表套字典，包括字段和值
    print("persons.values():", persons.values())  # 列表套字典
    print("persons.values('name', 'age'):", persons.values('name', 'age'))
    # values_list():  列表套元组, 只有值
    print("persons.values_list():", persons.values_list())
    print("persons.values_list('name', 'age'):", persons.values_list('name', 'age'))

    print('-' * 60)
    # filter(): 详细, 类似数据库中的where语句
    persons = PersonModel.objects.filter(age__in=[100, 200, 666, 777, 888])  # in
    # exclude(): 排除，取反的意思
    persons = PersonModel.objects.exclude(age__in=[100, 200, 666, 777, 888])  # not in
    persons = PersonModel.objects.filter(age__contains='6')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__contains='3')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__icontains='3')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__regex='^wu')  # 正则匹配，姓武的
    persons = PersonModel.objects.filter(name__iregex='^wu')  # 正则匹配，忽略大小写
    # persons = PersonModel.objects.filter(age__range=[200, 400])  # 200-400之间，两边都包含

    persons = PersonModel.objects.filter(name__startswith='wu')  # 以wu开头，忽略大小写
    persons = PersonModel.objects.filter(name__istartswith='wu')  # 以wu开头，忽略大小写
    persons = PersonModel.objects.filter(name__endswith='wu')  # 以wu结尾，忽略大小写
    persons = PersonModel.objects.filter(name__iendswith='wu')  # 以wu结尾，忽略大小写
    print(persons)

    # 聚合函数：max,min,sum
    result = PersonModel.objects.aggregate(Max('age'))  # 最大值  {'age__max': 666}
    result = PersonModel.objects.aggregate(Min('age'))  # 最小值  {'age__min': 100}
    result = PersonModel.objects.aggregate(Sum('age'))  # 求和  {'age__sum': 1666}
    result = PersonModel.objects.aggregate(Avg('age'))  # 平均值  {'age__avg': 333.2}
    result = PersonModel.objects.aggregate(Count('age'))  # 计数  {'age__count': 5}
    print(result)

    # 排序
    persons = PersonModel.objects.all().order_by('age')  # 升序
    persons = PersonModel.objects.all().order_by('age', '-id')  # 先按照age升序，如果age相同则按id降序排列
    persons = PersonModel.objects.all().order_by('-age')  # 降序
    print(persons)

    return HttpResponse('查询成功!')


# 分页功能
# 手动分页
def paginate(request, page=1):
    # 页码：page
    # 每页数量：per_page
    per_page = 10

    # 分页功能：
    #  数据 =【1,2,3,4,5,...,100】
    #   第几页       数据范围       数据下标范围      切片
    #   page=1        1 ~ 10      0 ~ 9        [0 : 10]
    #   page=2       11 ~ 20     10 ~ 19       [10 : 20]
    #   page=3       21 ~ 30     20 ~ 29       [20 : 30]
    #   page=4       31 ~ 40     30 ~ 39       [30 : 40]
    #   ...
    #   page=n                        [(n-1) * 10  :  n * 10]
    #   page=page                     [(page-1) * per_page  :  page * per_page]

    # 实现分页功能
    persons = PersonModel.objects.all()
    persons = persons[(page-1) * per_page  :  page * per_page]

    # 总页数
    total = PersonModel.objects.count()  # 总数据量
    total_page = math.ceil(total / per_page)  # 总页数
    pages = range(1, total_page+1)  # 1,2,3,4,5,6,7...

    data = {'persons': persons,'pages': pages}
    return render(request, 'paginate.html', data)


# 分页器：自动分页
from django.core.paginator import Paginator

def paginate2(request, page=1):
    per_page = 10

    all_data = PersonModel.objects.all()

    # 分页器
    paginator = Paginator(all_data, per_page)
    persons = paginator.page(page)  # 获取第page页的数据
    pages = paginator.page_range  # 页码范围，可以遍历

    data = {'persons': persons, 'pages': pages}
    return render(request, 'paginate2.html', data)


