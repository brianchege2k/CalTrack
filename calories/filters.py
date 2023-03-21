import django_filters
from django_filters import CharFilter
from .models import *

class FoodFilter(django_filters.FilterSet):
	food_name = CharFilter(field_name = 'name' , lookup_expr = 'icontains',label='Search food items')
	class Meta:
		model = Food
		fields = ['food_name']
class ExerciseFilter(django_filters.FilterSet):
	exercise_name = CharFilter(field_name = 'name' , lookup_expr = 'icontains',label='Search exercise items')
	class Meta:
		model = Exercise
		fields = ['exercise_name']
