from django.urls import path

# 导入courses报错，必须导入courses.views
import blog01.views
import courses.views

urlpatterns = [
    path('orm', blog01.views.orm)
]