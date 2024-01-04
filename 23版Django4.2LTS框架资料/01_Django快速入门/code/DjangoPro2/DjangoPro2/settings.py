from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 项目的密钥
SECRET_KEY = 'django-insecure-@o$)(@-s)t(jenz*5wbs^7-tohe)(d=equv7k3t4at6&2p9v_3'

# 是否调试模式
#  True: 表示调试模式，自动重启，一般用于开发过程中
#  False: 表示非调试模式，一般用于上线部署
DEBUG = True
# 被允许的域名或IP
#   *  : 表示通配符，匹配所有的IP,表示可以被其他任何电脑来访问我（局域网）
#  上线后可以指定其他哪些服务器来访问我
ALLOWED_HOSTS = ['*']

# 定义应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 定义自己的应用
    'user',
    'App',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由
ROOT_URLCONF = 'DjangoPro2.urls'

# 模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wsgi目录
WSGI_APPLICATION = 'DjangoPro2.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 密码验证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 国际化
LANGUAGE_CODE = 'zh-hans'  # en-us英语，zh-hans中文
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 静态文件 (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# 默认的主键字段类型
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



