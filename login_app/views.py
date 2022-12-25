from django.shortcuts import render, redirect
from .models import *
from the_wall_app.models import *
# register/login page
def index(request):
    return render(request, "login_app/index.html")

def display_user(request):
    # Don't allow a user who is not logged in to reach the /success route (i.e. by making a GET request in the address bar)
    if 'userid' in request.session:
        context={
            'user':User.objects.get(id=request.session['userid']),
            'messages': Message.objects.all().order_by("-created_at") ,
            'comments': Comment.objects.all(),
        }
        return render(request, "the_wall_app/user_page.html", context)
    return redirect("/")

def register(request):  
    if error_reg(request):
        return redirect("/")
    else:
        return redirect('/success')

def login(request):
    if error_log(request):
        return redirect("/")
    else: 
        return redirect('/success')

def logout(request):
    request.session.clear()	
    return redirect('/')