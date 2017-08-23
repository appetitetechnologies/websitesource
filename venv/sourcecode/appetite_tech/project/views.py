
from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models

def home(request):
    args={}
    return render(request,'home.html',args)

def projectlist(request,id=None):
    instance1 = models.Project.objects.all()
    instance=instance1.filter(cid = id)
    context ={"instance":instance}
    return render(request,"projectlist.html",context)

def projectdetail(request,id=None):
    instance = get_object_or_404(models.Project,id = id)
    context ={"instance":instance}
    return render(request,"projectdetail.html",context)