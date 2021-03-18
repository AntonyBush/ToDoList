from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Task
# Create your views here.


class CustomLoginView(LoginView):
    template_name='todo/login.html'
    fields='__all__'

    def get_success_url(self):
        return reverse_lazy('ToDoList')

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='task'

    def get_context_data(self, **kwargs):
        context= super().get_context_data( **kwargs)
        context['task']=context['task'].filter(user=self.request.user)   #filters only user's tasks
        context['count']=context['task'].filter(complete=True)
        return context
    #default template name='class_name.html' i.e task_list.html


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields= ['title','description','complete']
    success_url=reverse_lazy('ToDoList') #reverse on successful submission

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    #default template name='task_form.html'

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('ToDoList')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    template_name='todo/delete_task.html'
    success_url=reverse_lazy('ToDoList')