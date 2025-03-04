from rest_framework.views import APIView
from rest_framework.response import Response

from .models import FoodCategory
from .serializers import FoodListSerializer

class FoodCategoryListView(APIView):
    """
    Представление для вывода всех категорий меню с их блюдами.

    Отфильтровывает категории, в которых нет опубликованных блюд (is_publish=True).
    Включает только блюда с is_publish=True в каждой категории.

    Модель: FoodCategory
    Сериализатор: FoodListSerializer
    """
    def get(self, request):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        result = []
        for category in categories:
            foods = category.food.filter(is_publish=True)
            if foods.exists():
                category_data = FoodListSerializer(category).data
                category_data["foods"] = FoodListSerializer(category).fields["foods"].to_representation(foods)
                result.append(category_data)
        return Response(result)
