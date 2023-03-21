from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
from .models import Food,Profile,Exercise


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('food_selected','quantity',)

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name','quantity','calorie','fat','protein','carbohydrate')

class SelectExerciseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('exercise_selected','duration')

    def __init__(self, user, *args, **kwargs):
        super(SelectExerciseForm, self).__init__(*args, **kwargs)
        self.fields['exercise_selected'].queryset = Exercise.objects.filter(person_of=user)


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name','calorie','duration')
   
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('calorie_goal',)