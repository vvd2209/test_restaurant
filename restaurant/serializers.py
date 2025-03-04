from rest_framework import serializers
from .models import Food, FoodCategory

class FoodSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Food, предназначенный для представления информации о блюде.

    Атрибуты:
    - additional: Список дополнительных товаров, представленных как их внутренние коды.

    Модель: Food
    Поля: internal_code, code, name_ru, description_ru, description_en, description_ch, is_vegan,
           is_special, cost, additional
    """
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели FoodCategory, включающий список блюд из категории.

    Атрибуты:
    - foods: Список блюд, принадлежащих категории, представленных через FoodSerializer.

    Модель: FoodCategory
    Поля: id, name_ru, name_en, name_ch, order_id, foods
    """
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
