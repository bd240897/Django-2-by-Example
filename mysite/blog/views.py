from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

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
    # позволяет отображать несколько объектов любого типа.

    # переопределенный QuerySet модели вместо получения всех объектов
    queryset = Post.published.all()
    # переменная контекста HTML-шаблона
    context_object_name = 'posts'
    # использовать постраничное отображение по три объекта на странице;
    paginate_by = 3
    # использовать указанный шаблон для формирования страницы.
    template_name = 'blog/post/list.html'
    # УЧЕСТЬ ЧТО шаблон  постраничного вывода по умолчанию не ?page а ?page_obj

# стр - 49 - Обработка данных формы
# cnh - 51 - Отправка электронной почты с Django
def post_share(request, post_id):
    print('A am here', post_id)
    """
    Обработчик формы
    получает id статьи
    Один для отображения пустой формы и  обработки введенных данных
    """
    # Получение СТАТЬЕ по идентификатору.
    post = get_object_or_404(Post, id=post_id, status='published')
    # флаг - отпарвлено ли сообщение
    sent = False
    if request.method == 'POST': # если метод POST
        # получаем данные из request и создаем объект формы
        # Форма была отправлена на сохранение.
        form = EmailPostForm(request.POST)
        # проверка введенных данных T/F, ошибки в form.errors.
        if form.is_valid():
            # Если форма некорректна, мы возвращаем ее с введенными пользователем данными и сообщениями об ошибках
            # Все поля формы прошли валидацию - возвращается словарем с полями формы
            # Если форма не проходит валидацию, то в атрибут cleaned_data попадут только корректные поля.
            cd = form.cleaned_data
            # ... Отправка электронной почты.
            # Отправка электронной почты.
            post_url = request.build_absolute_uri(post.get_absolute_url()) # абсолютная ссылка на статью
            # достаем из полей формы - name email comments to - (см класс формы)
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            # отпарвить эмейл - аргументы - сообщение, отправителя и список получателей достаем из словаря формы cleaned_data['to']
            send_mail(subject, message, 'bd2408972@mail.ru', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    # Если метод запроса – GET - отображает пустую форму????????
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent' : sent})


# cтр - 58 - Обработка модельных форм
def post_detail(request, year, month, day, post):
    """
    Отобразить одну статью + комменты
    И отображает и выводит комменты
    """
    # запрос к базе данных
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # Список всех активных комментариев для этой статьи.
    # post.comments обращение к ПОСТУ по связанной таблице КОММЕНТ
    # --менеджер связанных объектов comments, определенный в модели Comment в аргументе related_name
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Пользователь отправил комментарий.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем обьект модели комментариев, но пока не сохраняем в базе данных при помощи commit=False.
            # перед сохранением объекта нам НУЖНО еще его изменить
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье.
            new_comment.post = post
            # Сохраняем комментарий в базе данных.
            new_comment.save()
    else:
        comment_form = CommentForm()
            # формирования HTML-шаблона
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


# ОСТЕНОВИЛСЯ НА "Добавление подсистемы тегов"