from django.urls import path

from .views import HomePageView,LoginPage,LogOutPage,select_food,add_food,select_exercise,add_exercise,RegisterPage,ProfilePage,update_food,delete_food,update_exercise,delete_exercise


urlpatterns = [
	path('', HomePageView,name='home'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	path('select_food/',select_food,name='select_food'),
	path('add_food/',add_food,name='add_food'),
    path('select_exercise/',select_exercise,name='select_exercise'),
	path('add_exercise/',add_exercise,name='add_exercise'),
	path('update_food/<str:pk>/',update_food,name='update_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
    path('update_exercise/<str:pk>/',update_exercise,name='update_exercise'),
	path('delete_exercise/<str:pk>/',delete_exercise,name='delete_exercise'),
	path('register/',RegisterPage,name='register'),
	path('profile/',ProfilePage,name='profile'),

  
]