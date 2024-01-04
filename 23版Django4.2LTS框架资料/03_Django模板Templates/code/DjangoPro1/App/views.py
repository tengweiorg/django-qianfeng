import datetime

from django.shortcuts import render

# 模板
def index(request):
    data = {
        'name': 'zhangsan',
        'age': 3,
        'likes': ['movie', 'game', 'code'],
        'address': {'city': '深圳', 'province': '广东'},
        'stars': [
            ['化腾', '马云', '斯克'],
            ['雷军', '彦宏', '一鸣'],
            ['伯格', '盖茨', '正非'],
        ],
        'dt': datetime.datetime.now(),
        'code': '<b>I am a good man</b>',
        'code2': '''<script>
                        var n=3;
                        while(n--) {
                            alert('哈哈')
                        }
                    </script>''',

    }
    return render(request, 'index.html', data)


# 模板继承
# 父模板
def block(request):
    return render(request, 'block.html')


# 子模板
def child(request):
    return render(request, 'child.html')


# 使用模板（HTML+模板语言）： 前后端不分离
