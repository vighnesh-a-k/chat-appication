from django.shortcuts import render,redirect
from .forms import RoomForm,messageForm,CustomSignupForm,loginForm
from django.views.generic import ListView, CreateView
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.http import JsonResponse

class ChatRoomListView(ListView):
    model = ChatRoom
    template_name = 'chatroom/room_list.html'


def create_message(request,pk):
    if request.method == 'POST':
        
        if request.POST.get('message'):
        
            Message.content=request.POST.get('message') 
            return redirect('create_message', room_id=pk)
            
    
    context={}
    
    obj = ChatRoom.objects.get(id=pk)
    context["name"]= obj.name
    return render(request, 'chatroom/chatroom.html', {'context': context})

def home(request):
     return render(request, 'chatroom/home.html')



def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('create_message', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'chatroom/room_create.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomSignupForm()

    return render(request, 'chatroom/signup.html', {'form': form})

def login(request):
    if request.method=="POST":
        form=loginForm
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            auth_login( request,user)
            return redirect('home')
    else:
         form = loginForm()

    return render(request, 'chatroom/login.html', {'form': form})


def logout_view(request):
    logout(request)

def search_user(request):
    if request.method=='POST':
        name=request.username
        result=User.objects.get(username=name)
        if result!=None:
             return JsonResponse({'message': 'success',"username":result})
        else:
            return JsonResponse({'message': 'failed'})






