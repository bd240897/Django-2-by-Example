# В ЭТОМ ФАЙЛЕ КАНОНИЧНО ОПИСЫВАТЬ ФОРМЫ
from django import forms
from .models import Comment

class EmailPostForm(forms.Form): # унаследованный от Form.
    """
    Класс Django-формы
    тут 4 поля: name email to comment
    """
    name = forms.CharField(max_length=25) # валидация полей - иначе forms.ValidationError.
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea) # необязательно поле

# стр - 58 - Создание модельных форм
class CommentForm(forms.ModelForm):
    """Форма для комментариев"""

    class Meta:
        # ссылка на модель БД - тут задаем поля
        model = Comment
        #  явно указать, какие использовать в форме, а какие – нет - доступны пользователю
        fields = ('name', 'email', 'body')