
from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Projects
# Create your views here.
def projects(request):
    if request.method == "POST":
        form = projectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProjectForm()
    return render(request,'index.html',{'form':form})
def show(request):
    context ={}

    # add the dictionary during initialization
    context["Projects"] = Projects.objects.all()

    return render(request, "show.html", context)



    #Project = Projects.objects.all()
    #return render(request,"show.html",{'Projects':Projects})
def add(request):
    context ={}

    # add the dictionary during initialization
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "add.html", context)
def edit(request, project_id):
    Projects = Projects.objects.get(id=project_id)
    return render(request,'edit.html', {'Projects':Projects})
def update(request, id):
    Projects = Projects.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance = project)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'Projects': Project})
def destroy(request, id):
    Projects = Projects.objects.get(id=project_id)
    Projects.delete()
    return redirect("/show")
