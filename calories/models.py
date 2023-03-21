from django.db import models
from django.contrib.auth.models import User

from datetime import date

# Create your models here.


class Food(models.Model):
	name = models.CharField(max_length=200 ,null=False)
	quantity = models.PositiveIntegerField(null=False,default=0)
	calorie = models.FloatField(null=False,default=0)
	fat = models.FloatField(null=False,default=0)
	protein = models.FloatField(null = False, default = 0)
	carbohydrate = models.FloatField(null=False, default= 0)
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Exercise (models.Model):
	name = models.CharField(max_length=200, null=False)
	calorie = models.FloatField(null=False, default=0)
	duration = models.FloatField(null= False,default=0)
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)


	def __str__(self):
		return self.name


class Profile(models.Model):
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    calorie_count = models.FloatField(default=0, null=True, blank=True)
    food_selected = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField(default=0)
    total_calorie = models.PositiveIntegerField(default=0, null=True)
    date = models.DateField(auto_now_add=True)
    calorie_goal = models.PositiveIntegerField(default=0)
    total_calorie_burned = models.PositiveIntegerField(default=0)
    exercise_selected = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.FloatField(default=0, null=True, blank=True)
    all_food_selected_today = models.ManyToManyField(Food, through='PostFood', related_name='inventory')
    all_exercises_selected_today = models.ManyToManyField(Exercise, through='PostExercise', related_name='exercises')


    def save(self, *args, **kwargs):
        if self.food_selected:
            self.amount = self.food_selected.calorie / self.food_selected.quantity
            self.calorie_count = self.amount * self.quantity
            self.total_calorie += self.calorie_count
            calories = Profile.objects.filter(person_of=self.person_of).last()
            PostFood.objects.create(profile=calories, food=self.food_selected, calorie_amount=self.calorie_count, amount=self.quantity)
            self.food_selected = None

        if self.exercise_selected:
            self.calories_burned = (self.exercise_selected.calorie / self.exercise_selected.duration) * self.duration
            self.total_calorie_burned += self.calories_burned
            calories = Profile.objects.filter(person_of=self.person_of).last()
            PostExercise.objects.create(profile=calories, exercise=self.exercise_selected, calorie_burned=self.calories_burned, duration=self.duration)
            self.exercise_selected = None

        super(Profile, self).save(*args, **kwargs)

def __str__(self):
    if self.person_of:
        return str(self.person_of.username)
    else:
        return 'No user'


class PostFood(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    calorie_amount = models.PositiveIntegerField(default=0,null=True,blank=True)
    amount = models.FloatField(default=0)
    

class PostExercise(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	calorie_burned = models.PositiveIntegerField(default=0, null= True, blank=True)
	duration = models.FloatField(default=0)