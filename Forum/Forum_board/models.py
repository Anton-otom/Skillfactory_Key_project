from django.db import models

from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field


# Модель для пользователя форума.
class UserF(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


# Класс с вариантами категорий объявлений на форуме.
# Второе значение переменной хранится в "label".
class Category(models.TextChoices):
    TANKS = 'Tanks', 'Танки'
    HEALS = 'Heals', 'Хилы'
    DD = 'DD', 'ДД'
    MERCHANTS = 'Merchants', 'Торговцы'
    GUILDMASTERS = 'Guildmasters', 'Гилдмастеры'
    QUESTGIVERS = 'Questgivers', 'Квестгиверы'
    BLACKSMITHS = 'Blacksmiths', 'Кузнецы'
    TANNERS = 'Tanners', 'Кожевники'
    ALCHEMISTS = 'Alchemists', 'Зельевары'
    SPELLMASTERS = 'Spellmasters', 'Мастера заклинаний'


# Модель для объявления на форуме.
class Statement(models.Model):
    author = models.ForeignKey(UserF, on_delete=models.CASCADE, related_name='statements')
    category = models.CharField(max_length=20, choices=Category.choices)
    title = models.CharField(max_length=60)
    text = models.TextField()
    attachments = CKEditor5Field('Content', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)


# Модель для откликов на объявления на форуме.
class Reaction(models.Model):
    author = models.ForeignKey(UserF, on_delete=models.CASCADE, related_name='reactions')
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE, related_name='reactions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)