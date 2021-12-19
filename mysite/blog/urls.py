from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
            # path('', views.post_list, name='post_list'), # отображение странц через фукнцию
            # автоматом передается параметр ?page=1 в строке браузера
            path('', views.PostListView.as_view(), name='post_list'), # отображение страниц через класс
            path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
            path('<int:post_id>/share/', views.post_share, name='post_share'), # отправка эмейла
            ]

# "^(year)/(month)/(day)/(post)/"