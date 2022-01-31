# КАРТА САЙТА ДЛЯ ПОИСКА
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """Карта сайта"""

    # частоту обновления страниц статей и степень их совпадения с тематикой сайта
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        """Возвращает QuerySet объектов, которые будут отображаться в карте сайта"""
        # По умолчанию Django использует метод get_absolute_url() объектов списка, чтобы получать их URL’ы.
        return Post.published.all()

    def lastmod(self, obj):
        """возвращает время последней модификации статьи"""
        return obj.updated