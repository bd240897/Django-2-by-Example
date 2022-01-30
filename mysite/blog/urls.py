from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
            # отображение странц через фукнцию
            # автоматом передается параметр ?page=1 в строке браузера
            path('', views.post_list, name='post_list'),
            # отображение странц через класс
            # path('', views.PostListView.as_view(), name='post_list'), # отображение страниц через класс
            path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
            # отправка эмейла
            path('<int:post_id>/share/', views.post_share, name='post_share'),
            # работа с тегами
            path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag')
            ]

# "^(year)/(month)/(day)/(post)/"