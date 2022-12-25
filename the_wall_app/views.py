from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def post_message(request):
    create_message(request)
    return redirect('/success')

def post_comment(request):
    create_comment(request)
    return redirect('/success')

def delete_message(request):
    del_message(request)
    return redirect('/success')