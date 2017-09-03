
from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ProjectCreateForm
from . import models

def home(request):
    args={}
    return render(request,'index.html',args)

def projectlist(request,id=None):
    instance1 = models.Project.objects.all()
    instance=instance1.filter(cid = id)
    context ={"instance":instance}
    return render(request,"projectlist.html",context)

def projectdetail(request,id=None):
    instance = get_object_or_404(models.Project,id = id)
    context ={"instance":instance}
    return render(request,"projectdetail.html",context)

def ProjectCreate(request):
    form = ProjectCreateForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context={'hello':"PROJECT SUCCESSFULLY SUBMITTED"}
        return render(request, 'projectcreatesuccess.html', context)

        #form="submitted successfully"
    context = {'form':form,
               'hello':'hi',
               }
    return render(request,'projectcreate.html',context)