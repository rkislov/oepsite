from django.db import models
import uuid

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в социальной сети',
        unique=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


    def __str__(self):
        return f'#{self.external_id} {self.name}'


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(
        Profile,
        verbose_name='Профиль',
        on_delete=models.PROTECT
    )
    text = models.TextField(
        verbose_name="Текст"
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    
    class Meta:
        verbose_name='Сообщениe'
        verbose_name_plural = 'Сообщения'