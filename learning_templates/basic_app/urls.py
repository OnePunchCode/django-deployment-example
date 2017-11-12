from django.conf.urls import url
from basic_app import views

# Template tagging 这里app_name是template的专有标签，用于在html pages中获取html的相对路径
# 需要一个名字来标注路径
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]