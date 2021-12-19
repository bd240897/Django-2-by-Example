# В ЭТОМ ФАЙЛЕ КАНОНИЧНО ОПИСЫВАТЬ ФОРМЫ
from django import forms


class EmailPostForm(forms.Form): # унаследованный от Form.
    """
    Класс Django-формы
    тут 4 поля: name email to comment
    """
    name = forms.CharField(max_length=25) # валидация полей - иначе forms.ValidationError.
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea) # необязательно поле