from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
            # post views
            # path('', views.post_list, name='post_list'), # отображение странц через фукнцию
            path('', views.PostListView.as_view(), name='post_list'), # отображение страниц через класс
            path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
            ]

# "^(year)/(month)/(day)/(post)/"