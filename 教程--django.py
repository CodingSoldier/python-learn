#####安装Django
pip install django==2.0

#验证安装是否完成
django-admin  

# 查看版本
python -m django --version 

# django命令
# 创建django项目
django-amdin startproject django_introduction 

# 导入项目到pycharm
pycharm -> open —> django_introduction

manage.py    项目管理文件
settings.py  配置文件
urls.py      路由文件
wsgi.py      wsgi应用配置文件

# 运行django，解析器要选择原始的Python3.7
python  manage.py runserver

django应用 VS django项目
	一个django项目就是一个基于django的web应用
	一个django应用就是一个可重用的python软件包，不可直接运行

每个应用管理模型、视图、模板、路由、静态文件；模型、视图、模板、路由、静态文件是应用范围的概念
一个django项目包含一组配置和若干个django应用

# 创建blog应用，多了一个blog目录
python manage.py startapp blog

# django应用目录介绍
views.py    视图处理
models.py   应用模型
admin.py    Admin模块管理对象
apps.py     声明应用
tests.py    测试用例
urls.py     路由（自行创建）


hello world页面
django_introduction
	1、settings.py -> INSTALLED_APPS 加入 'blog.apps.BlogConfig'
	   # blog.apps.BlogConfig是blog/apps.py中的class
	2、urls.py 的urlPatterns加入 path('blog/', include('blog.urls'))

blog
	1、views.py新增函数
		def hello_world(request):
		    return HttpResponse("Hello World")
	2、新建urls.py文件
		urlpatterns = [
		    path("hello_world", blog.views.hello_world)
		]

访问 http://127.0.0.1:8000/blog/hello_world		

模型层
blog -> models.py 新建class

python manage.py makemigrations
# 在migrations下生成数据库要执行的内容
 
python manage.py migrate
# 执行migrations下的内容
# 记录操作到django_migrations表中

删除模型类：
1、删除模型类代码
2、删除migrations文件
3、删除django_migrations表的记录
4、删除数据表

pycharm配置sql连接
Comment: settings.py全路径
File: db.sqlite3全路径


进入django shell环境，小范围调试
python manage.py shell

from blog.models import Article
a.title = "title02"
a = Article()
a.brief_content = "brief02"
a.content = 'content02'

a.save()

articles = Article.objects.all()
article = articles[0]
print(article.title)


django admin  后台管理模块
python manage.py createsuperuser
用户 admin
邮箱不填
密码 adminadmin

python manage.py runserver

http://127.0.0.1:8000/admin/login/

# 注册Article模块，blog -> amdin.py
admin.site.register(Article)
# 导入模块前面要加 .

在 http://127.0.0.1:8000/admin/login/ 中新增article

新增文章报错了 ￣□￣｜｜


blog/views.py 新增article_content
blog/urls.py  新增path("article1", blog.views.article_content)

http://127.0.0.1:8000/blog/article1  获取数据库数据


使用模板
views.py新增函数
def get_index_page(request):
    all_article = Article.objects.all()
    # 返回模板与变量
    return render(request, 'blog/index.html', {'article_list': all_article})

增加路由
	path("index", blog.views.get_index_page)


获取请求参数
url   path('detail/<int:article_id>', blog.views.get_detail_page)
函数  def get_detail_page(request, article_id)


获取get请求参数
http://127.0.0.1:8000/blog/index?page=2
page = request.GET.get('page')


分页
    paginator = Paginator(all_article, 10)
    print('page num:', paginator.num_pages)
    page_article_list = paginator.page(page)
    print("数据", page_article_list)

http://127.0.0.1:8000/blog/index?page=1


# 排序，publish_date倒序
top10_article_list = Article.objects.order_by('-publish_date')[:2]

















