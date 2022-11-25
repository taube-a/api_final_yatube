from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Таблица Группы."""
    title = models.CharField(
        'Название группы', max_length=200, unique=True)
    slug = models.SlugField('Адрес', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'сообщества'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Таблица Посты."""
    text = models.TextField(
        'Текст поста', help_text='Введите текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу')
    image = models.ImageField(
        'Картинка', upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Таблица Комментарии.."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Таблица Подписки."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='follower')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='following')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'), name='unique_following')]

    def __str__(self):
        return f'{self.user} подписан на пользователя {self.following}'
