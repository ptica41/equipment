from django.db import models


class Main(models.Model):
    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    num = models.CharField(verbose_name='№ п/п в 804 приказе')
    name_804 = models.CharField(verbose_name='Наименование в 804 приказе', blank=True, null=True)
    name_provider = models.CharField(verbose_name='Наименование у поставщика')
    provider = models.CharField(verbose_name='Поставщик')
    cost = models.IntegerField(verbose_name='Стоимость')
    size = models.CharField(verbose_name='Размер', blank=True, null=True)
    article = models.CharField(verbose_name='Артикул', blank=True, null=True)
    link = models.CharField(verbose_name='Ссылка на товар у поставщика', blank=True, null=True)
    img = models.TextField(verbose_name='Фото (ссылка)', blank=True, null=True)

    class Meta:
        db_table = 'Main'
        verbose_name_plural = 'Главная'
        ordering = ['num']
