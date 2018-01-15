from django.conf.urls import url
from . import views

app_name='learning_logs'
urlpatterns = [
    
    url(r'^$',views.index,name='index'),
    url(r'^topics/$',views.topics,name='topics'),
]
