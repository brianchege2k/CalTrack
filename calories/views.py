from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SelectFoodForm,AddFoodForm,CreateUserForm,ProfileForm,SelectExerciseForm,AddExerciseForm
from .models import *
from datetime import timedelta
from django.utils import timezone
from datetime import date
from datetime import datetime
from .filters import FoodFilter,ExerciseFilter
from django.utils import timezone


@login_required(login_url='login')
def HomePageView(request):
    #taking the latest profile object
    profile = Profile.objects.filter(person_of=request.user).last()
    calorie_goal = profile.calorie_goal

    #creating one profile each day
    today = timezone.now().date()
    if profile.date != today:
        new_profile = Profile.objects.create(person_of=request.user)
        profile = new_profile

    # showing all food consumed and exercises done today
    all_food_today = PostFood.objects.filter(profile=profile)
    all_exercises_today = PostExercise.objects.filter(profile=profile)

    # calculating total calorie intake and burned calories from exercises
    total_calorie_intake = sum(food.calorie_amount for food in all_food_today)
    total_calorie_burned = sum(exercise.calorie_burned for exercise in all_exercises_today)
    profile.total_calorie_burned = total_calorie_burned
    profile.save()

    # calculating calorie goal status and over calorie count
    calorie_goal_status = calorie_goal - total_calorie_intake + total_calorie_burned
    over_calorie = max(0, calorie_goal_status)

    context = {
        'total_calorie_intake': total_calorie_intake,
        'total_calorie_burned': total_calorie_burned,
        'calorie_goal': calorie_goal,
        'calorie_goal_status': calorie_goal_status,
        'over_calorie': over_calorie,
        'food_selected_today': all_food_today,
        'exercises_done_today': all_exercises_today,
    }
    print("Number of PostFood objects today: ", all_food_today.count())
    print("Number of PostExercise objects today: ", all_exercises_today.count())

    return render(request, 'home.html', context)


#signup page
def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,"Account was created for "+ user)
				return redirect('login')

		context = {'form':form}
		return render(request,'register.html',context)

#login page
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
#login page
def LoginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Username or password is incorrect')
		context = {}
		return render(request,'login.html',context)

#logout page
def LogOutPage(request):
	logout(request)
	return redirect('login')

#####################################  FOOD VIEWS ###########################

#for selecting food each day
@login_required
def select_food(request):
	person = Profile.objects.filter(person_of=request.user).last()
	#for showing all food items available
	food_items = Food.objects.filter(person_of=request.user)
	form = SelectFoodForm(request.user,instance=person)

	if request.method == 'POST':
		form = SelectFoodForm(request.user,request.POST,instance=person)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = SelectFoodForm(request.user)

	context = {'form':form,'food_items':food_items}
	return render(request, 'select_food.html',context)

#for adding new food
def add_food(request):
	#for showing all food items available
	food_items = Food.objects.filter(person_of=request.user)
	form = AddFoodForm(request.POST) 
	if request.method == 'POST':
		form = AddFoodForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.person_of = request.user
			profile.save()
			return redirect('add_food')
	else:
		form = AddFoodForm()
	#for filtering food
	myFilter = FoodFilter(request.GET,queryset=food_items)
	food_items = myFilter.qs
	context = {'form':form,'food_items':food_items,'myFilter':myFilter}
	return render(request,'add_food.html',context)

#for updating food given by the user
@login_required
def update_food(request,pk):
	food_items = Food.objects.filter(person_of=request.user)

	food_item = Food.objects.get(id=pk)
	form =  AddFoodForm(instance=food_item)
	if request.method == 'POST':
		form = AddFoodForm(request.POST,instance=food_item)
		if form.is_valid():
			form.save()
			return redirect('profile')
	myFilter = FoodFilter(request.GET,queryset=food_items)
	context = {'form':form,'food_items':food_items,'myFilter':myFilter}

	return render(request,'add_food.html',context)

#for deleting food given by the user
@login_required
def delete_food(request,pk):
	food_item = Food.objects.get(id=pk)
	if request.method == "POST":
		food_item.delete()
		return redirect('profile')
	context = {'food':food_item,}
	return render(request,'delete_food.html',context)
#############################################

#######################    EXERCISE VIEWS #######################
#for selecting exercises each day
@login_required
def select_exercise(request):
	person = Profile.objects.filter(person_of=request.user).last()
	#for showing all Exercise items available
	exercise_items = Exercise.objects.filter(person_of=request.user)
	form = SelectExerciseForm(request.user,instance=person)

	if request.method == 'POST':
		form = SelectExerciseForm(request.user,request.POST,instance=person)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = SelectExerciseForm(request.user)

	context = {'form':form,'exercise_items':exercise_items}
	return render(request, 'select_exercise.html',context)

#for adding new food
def add_exercise(request):
	#for showing all exercises items available
	exercise_items = Exercise.objects.filter(person_of=request.user)
	form = AddExerciseForm(request.POST) 
	if request.method == 'POST':
		form = AddExerciseForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.person_of = request.user
			profile.save()
			return redirect('add_exercise')
	else:
		form = AddExerciseForm()
	#for filtering food
	myFilter = ExerciseFilter(request.GET,queryset=exercise_items)
	exercise_items = myFilter.qs
	context = {'form':form,'exercise_items':exercise_items,'myFilter':myFilter}
	return render(request,'add_exercise.html',context)

#for updating exercise given by the user
@login_required
def update_exercise(request,pk):
	exercise_items = Exercise.objects.filter(person_of=request.user)

	exercise_item = Exercise.objects.get(id=pk)
	form =  AddExerciseForm(instance=exercise_item)
	if request.method == 'POST':
		form = AddExerciseForm(request.POST,instance=exercise_item)
		if form.is_valid():
			form.save()
			return redirect('profile')
	myFilter = ExerciseFilter(request.GET,queryset=exercise_items)
	context = {'form':form,'exercise_items':exercise_items,'myFilter':myFilter}

	return render(request,'add_exercise.html',context)

#for deleting exercises given by the user
@login_required
def delete_exercise(request,pk):
	exercise_item = Exercise.objects.get(id=pk)
	if request.method == "POST":
		exercise_item.delete()
		return redirect('profile')
	context = {'exercise':exercise_item,}
	return render(request,'delete_exercise.html',context)


#################################################################################

#profile page of user
@login_required
def ProfilePage(request):
	#getting the lastest profile object for the user
	person = Profile.objects.filter(person_of=request.user).last()
	food_items = Food.objects.filter(person_of=request.user)
	exercise_items = Exercise.objects.filter(person_of=request.user)
	form = ProfileForm(instance=person)

	if request.method == 'POST':
		form = ProfileForm(request.POST,instance=person)
		if form.is_valid():	
			form.save()
			return redirect('profile')
	else:
		form = ProfileForm(instance=person)

	#querying all records for the last seven days 
	some_day_last_week = timezone.now().date() -timedelta(days=7)
	records=Profile.objects.filter(date__gte=some_day_last_week,date__lt=timezone.now().date(),person_of=request.user)
	context = {'form': form, 'food_items': food_items, 'exercise_items': exercise_items, 'records': records}
	return render(request, 'profile.html',context)


