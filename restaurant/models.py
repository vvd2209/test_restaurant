from django.db import models
from model_utils.models import TimeStampedModel

class FoodCategory(TimeStampedModel):
    """
    Модель, представляющая категорию блюд в меню ресторана.

    Атрибуты:
    - name_ru: Название категории на русском языке.
    - name_en: Название категории на английском языке (необязательное).
    - name_ch: Название категории на китайском языке (необязательное).
    - order_id: Порядковый номер для сортировки категорий меню.

    Методы:
    - __str__: Возвращает название категории на русском языке.
    """

    name_ru = models.CharField(verbose_name='Название на русском', max_length=255, unique=True)
    name_en = models.CharField(verbose_name='Название на английском', max_length=255, unique=True, blank=True, null=True)
    name_ch = models.CharField(verbose_name='Название на китайском', max_length=255, unique=True, blank=True, null=True)
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')

    def __str__(self):
        return self.name_ru


class Food(TimeStampedModel):
    """
    Модель, представляющая конкретное блюдо в меню ресторана.

    Атрибуты:
    - category: Категория, к которой принадлежит блюдо.
    - is_vegan: Флаг, указывающий, является ли блюдо вегетарианским.
    - is_special: Флаг, указывающий, является ли блюдо специальным предложением.
    - code: Код блюда в системе поставщика.
    - internal_code: Внутренний код блюда в приложении (уникальный).
    - name_ru: Название блюда на русском языке.
    - description_ru: Описание блюда на русском языке.
    - description_en: Описание блюда на английском языке (необязательное).
    - description_ch: Описание блюда на китайском языке (необязательное).
    - cost: Цена блюда.
    - is_publish: Флаг, указывающий, опубликовано ли блюдо.
    - additional: Дополнительные товары, связанные с блюдом (связь многие ко многим).

    Методы:
    - __str__: Возвращает название блюда на русском языке.
    """
    category = models.ForeignKey(FoodCategory, related_name='food', on_delete=models.CASCADE)

    is_vegan = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)

    code = models.IntegerField(verbose_name='Код поставщика')
    internal_code = models.IntegerField(unique=True, null=True, blank=True)

    name_ru = models.CharField(max_length=255)
    description_ru = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    description_ch = models.CharField(max_length=255, blank=True, null=True)

    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_publish = models.BooleanField(default=True)

    additional = models.ManyToManyField('self', symmetrical=False, related_name='additional_from', blank=True)

    def __str__(self):
        return self.name_ru