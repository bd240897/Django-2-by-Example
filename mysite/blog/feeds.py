# Добавление RSS для статей - новости об неовлениях

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    """"""

    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        """получает объекты, которые будут включены в рассылку."""
        return Post.published.all()[:5]

    def item_title(self, item):
        """получает для каждого объекта из результата items() заголовок и описание."""
        return item.title

    def item_description(self, item):
        """получает для каждого объекта из результата items()  описание."""
        # truncatewords, чтобы ограничить описание статей тридцатью словами
        return truncatewords(item.body, 30)
