from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """ Модель группы. """
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        blank=True,
        null=True)
    description = models.TextField('Описание', blank=True, null=True,)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        """ Мета-класс группы,
        описывающий 'нормальное' название и сортировку. """
        verbose_name = 'Group'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу!')

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        unique_together = 'user', 'following'
