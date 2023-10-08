from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import TaskForm
from .models import TaskModel
from django.views import View
from .serializers import TaskSerializer
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.
class HomeView(ListView):
    model=TaskModel
    template_name='taskapp/home.html'
    
"""def register(request):
    return render(request, template_name='taskapp/registration.html')
def login(request):
    return render(request, template_name='taskapp/login.html')
    """


def login(request):
    if request.method=='GET':
        return render(request, template_name='taskapp/login.html')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('items')
        else:
            return redirect('login')

def register(request):
    if request.method =='GET':
        return render(request, template_name='taskapp/registration.html')
    
    if request.method=='POST':

        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')


class TaskView(ListView):
    model=TaskModel
    template_name='taskapp/task.html'
    queryset=TaskModel.objects.all()
    context_object_name='tasks'
    
"""class TitleSearch(ListView):
    model=TaskModel
    template_name='taskapp/task.html'
    context_object_name='tasks'
    def get_queryset(self):
        search_input=self.request.GET.get('searchtitle')
        return TaskModel.objects.filter(title__icontains=search_input)"""
    
class OneTask(View):
    def get(self,request,pk):
        task_info=TaskModel.objects.get(id=pk)
        return render(request,'taskapp/onetask.html',{'onetask':task_info})
    

class DeleteTask(View):
    def post(self, request):
        delete_data=request.POST
        id=delete_data.get('id')
        task_delete=TaskModel.objects.get(id=id)
        task_delete.delete()
        return redirect('/task/')




class CreateTask(View):
    def get(self, request):
        form=TaskForm
        return render(request,'taskapp/createtask.html',{'form':form})
    def post(self, request):
        form=TaskForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()

        return HttpResponseRedirect('/')
    
class UpdateTask(View):
    def get(self, request,pk):
        info=TaskModel.objects.get(id=pk)
        fm=TaskForm(instance=info)
        return render(request,'taskapp/update.html',{'form':fm})
    def post(self, request, pk):
        info=TaskModel.objects.get(id=pk)
        fm=TaskForm(request.POST,request.FILES,instance=info)
        if fm.is_valid:
            fm.save()
        return redirect('/task/')
    

class TaskApi(APIView):
    def get(self, request,pk=None,format=None):
        taskid=pk
        if taskid is not None:
            tasks=TaskModel.objects.get(id=taskid)
            serializer=TaskSerializer(tasks)
            return Response(serializer.data)
        
        tasks=TaskModel.objects.all()
        serializer=TaskSerializer(tasks)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Data created Successfully'})

        return Response(serializer.errors)
    
    def put(self, request,pk=None,format=None):
        taskid=pk
        tasks=TaskModel.objects.get(pk=taskid)
        serializer=TaskSerializer(tasks,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Data is completely updated Successfully'})
        
        return Response(serializer.errors)
    
    def patch(self, request,pk=None,format=None):
        taskid=pk
        tasks=TaskModel.objects.get(pk=taskid)
        serializer=TaskSerializer(tasks,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Data is pertially updated Successfully'})
        
        return Response(serializer.errors)






    def list(self, requets):
        task=TaskModel.objects.all()
        serializer=TaskSerializer(task, many=True)
        return Response(serializer.data)
    

    def get(self,request,pk=None):
        id=request.data.get('id')
        if id is not None:
            task=TaskModel.objects.all()
            serializer=TaskSerializer(task, many=True)
            return Response(serializer.data)
        
    def create(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'sucessfully created'})
        return Response(serializer.errors)
    
    def update(self,request,pk):
        id=pk

        task=TaskModel.objects.get(pk=id)
        serializer=TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"updated"})
        return Response(serializer.errors)
    
    def partial_update(self, request,pk):
        id=pk

        task=TaskModel.objects.get(pk=id)
        serializer=TaskSerializer(task, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"partial"})
        return Response(serializer.errors)
    


    def delete(self,request, pk):
        id=pk
        stu=TaskModel.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"deleted"})
