from django.db import models


# Create your models here.

class InfBlock(models.Model):
    block_height = models.IntegerField('Высота блока')
    block_hash = models.TextField('Хэш блока')
    block_time = models.IntegerField('Время блока', default=None)
    block_address = models.TextField('Адрес майнера', max_length=60)
    block_numbers = models.IntegerField('Кол-во транзакций')

    def __str__(self):
        return self.block_address

    class Meta:
        verbose_name = 'Адрес майнера'
        verbose_name_plural = 'Адреса майнеров'
