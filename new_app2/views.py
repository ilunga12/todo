from django.shortcuts import render, redirect

from new_app2.forms import TodoForm
from new_app2.models import todo


# Create your views here.
def dad(request):
    return render(request,"hy.html")
#create
def create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request,"FORM.html",{"form":form})