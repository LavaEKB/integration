from django.db import models

class BufferFood(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=250, blank=False, null=False)

    # Relationships
    #restaurant = models.ForeignKey("organization.Restaurant", verbose_name='Ресторан', on_delete=models.CASCADE, related_query_name='foods')
    #category = models.ForeignKey("menu.Category", verbose_name='Категория', on_delete=models.DO_NOTHING, null=True, blank=True)

    # Fields
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    status = models.BooleanField(verbose_name="Статус (активный)", default=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="upload/images/food/", max_length=250,
                              blank=True, null=True)

    priority = models.PositiveIntegerField(verbose_name='Приоритет', default=1, null=False, blank=False) # убрал валидаторы
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    weight = models.PositiveIntegerField(verbose_name="Вес", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Temp Fields
    restaurant = models.CharField(verbose_name="id_организации", max_length=250, blank=False, null=False)
    category = models.CharField(verbose_name="Категории", max_length=250, blank=True, null=True)


    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return str(self.name)


class СompoundSettings(models.Model):
    #restaurant = models.ForeignKey("organization.Restaurant", verbose_name='Ресторан', on_delete=models.CASCADE, related_query_name='foods')

    APP_COMPAUND = [
        ('Iiko', 'Айко'),
        ('R_Keeper', 'Р-Kипер'),
    ]
    
    app_compaunds = models.CharField(
        max_length=8,
        choices=APP_COMPAUND,
        default='Iiko',
    )
    restaurant = models.CharField(verbose_name="id_организации", max_length=250, blank=False, null=False)
    user_id = models.CharField(verbose_name="Логин", max_length=250, blank=True, null=True)
    user_secret = models.CharField(verbose_name="Пароль", max_length=250, blank=True, null=True)
    api_key = models.CharField(verbose_name="API ключ", max_length=500, blank=True, null=True)
    url_token = models.URLField(verbose_name="URL токен", max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'подключение'
        verbose_name_plural = 'Установки подключений'

    def __str__(self):
        return str(self.app_compaunds)