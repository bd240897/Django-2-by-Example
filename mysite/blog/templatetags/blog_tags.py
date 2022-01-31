from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    """Простой тег который возвращает количетсво поубликованных статей"""

    # делает запрос к БД
    return Post.published.count()

# регистрируем и указываем шаблон, который будет использоваться для формирования HTML.
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    # Инклюзивные теги должны возвращать только словари контекста
    return {'latest_posts': latest_posts}
    #  Чтобы задать любое другое количество статей{% show_latest_posts 3 %}
    # учти у тега свой привязаный шаблок latest_posts.html - и когда мы ставляем тег он приятгивает этот шаблон к странице (круто)

@register.simple_tag
def get_most_commented_posts(count=5):
    """тег для отображения статей с наибольшим количеством комментариев"""
    # добавялем к какжлой статье новое поле - количество комментариев total_comments при помощи annotate
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    # mark_safe, чтобы пометить результат работы фильтра как HTML-код
    return mark_safe(markdown.markdown(text))