from django.db import models
from login_app.models import *
# Create your models here.
class Message(models.Model):
    user=models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user=models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message=models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def create_message(request):
    Message.objects.create(message=request.POST['message'],user=User.objects.get(id=request.POST['user']))

def create_comment(request):
    Comment.objects.create(comment=request.POST['comment'],user=User.objects.get(id=request.POST['user']),message=Message.objects.get(id=request.POST['message']))

def del_message(request):
    Message.objects.get(id=request.POST['message']).delete()