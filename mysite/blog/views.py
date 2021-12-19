from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

## стр 41 - Создание обработчиков списка и страницы подробностей
# def post_list(request):
#     """Отображение списка статей - первая версия"""
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})

# # стр 44 - Добавление постраничного отображения
# def post_list(request):
#     """Постраничное отображение нескольких статье - класс-пагинатор - версия 2"""
#     # ОСТАНОВИЛСЯ НА Создание HTML-шаблонов для обработчиков
#
#     object_list = Post.published.all()
#     # 1.инициализируем объект класса Paginator, указав количество объектов на одной странице
#     paginator = Paginator(object_list, 3) # По 3 статьи на каждой странице.
#     # 2.извлекаем из запроса GET-параметр page, который указывает текущую страницу
#     page = request.GET.get('page') # номер страницы, одна странцы = 3 статьи
#     print(page)
#     try:
#         # 3.получаем список объектов на нужной странице - на стрнице под номер page
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, возвращаем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'blog/post/list.html', {'page': page, 'posts': posts})

# стр 41 - Создание обработчиков списка и страницы подробностей
def post_detail(request, year, month, day, post):
    """Отобразить одну статью"""
    # запрос к базе данных
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # формирования HTML-шаблона
    return render(request, 'blog/post/detail.html', {'post': post})


# стр 46 - Использование обработчиков-классов
class PostListView(ListView):
    """Аналог функции post_list только в виде класса - ЭТО ПАГИНАТОР-КЛАСС"""
    # переопределенный QuerySet модели вместо получения всех объектов
    queryset = Post.published.all()
    # переменная контекста HTML-шаблона
    context_object_name = 'posts'
    # использовать постраничное отображение по три объекта на странице;
    paginate_by = 3
    # использовать указанный шаблон для формирования страницы.
    template_name = 'blog/post/list.html'