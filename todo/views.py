from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .models import Task
# Create your views here.
class UserRegForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomLoginView(LoginView):
    template_name='todo/login.html'
    fields='__all__'

    def get_success_url(self):
        return reverse_lazy('ToDoList')

class RegisterView(FormView):
    template_name='todo/register.html'
    form_class=UserRegForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('ToDoList')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('TodoList')
        return super(RegisterView,self).get( *args, **kwargs)  #if not authenticated


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='task'

    def get_context_data(self, **kwargs):
        context= super().get_context_data( **kwargs)
        context['task']=context['task'].filter(user=self.request.user)   #filters only user's tasks
        context['count']=context['task'].filter(complete=False).count()

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['task']=context['task'].filter(title__startswith=search_input)

        context['search_input']=search_input
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
    fields=['title','description','complete']
    success_url=reverse_lazy('ToDoList')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    template_name='todo/delete_task.html'
    success_url=reverse_lazy('ToDoList')