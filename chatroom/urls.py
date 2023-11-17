from django.urls import path
from . import views


urlpatterns = [
    path('rooms/', views.ChatRoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', views.create_message, name='create_message'),
    path('create-room/', views.create_room, name='create_room'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
     path('logout/', views.logout_view, name='logout'),
     path('user_search/', views.user_search, name='logout'),

    
    

]