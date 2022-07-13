import imp
from wsgiref.util import request_uri
from django import urls
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.http.response import HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView,\
    View, ListView, DeleteView
from django.http import HttpResponseNotFound, JsonResponse
from .models import Lista, Task
from .forms import ListaForm, TaskForm
from .mixins import AjaxableResponseMixin

def homeView(request):
    ctx={}
    user = request.user
    listas=[]
    if  not request.user.is_anonymous :
        listas= Lista.objects.filter(author=user)
    ctx['listas']=listas
    return render(request,'home.html',ctx)

# list CRUD

class NewListView(CreateView):
    form_class = ListaForm
    template_name = 'lists/new_list.html'
    def form_valid(self, form):
        if Lista.objects.filter(title=form['title']).exists():
            return HttpResponseForbidden ('You created a list with the same name before')
        else:
            blog_obj = form.save(commit=False)
            blog_obj.author = self.request.user
            blog_obj.slug = slugify(blog_obj.title)
            blog_obj.save()
            return HttpResponseRedirect(reverse('home'))
        
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewListView, self).dispatch(request, *args, **kwargs)


class ListDetailView(DetailView):
    model = Lista
    template_name = 'lists/list_details.html'
    context_object_name='lista'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(lista=self.object).order_by('-periority','timing')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListDetailView, self).dispatch(request, *args, **kwargs)


class UpdateListView(UpdateView):
    form_class = ListaForm
    template_name = 'lists/new_list.html'
    model = Lista

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        lis = Lista.objects.get(id=self.kwargs['pk'])
        author = lis.author
        print(user, author)
        if user != author:
            return HttpResponseForbidden ('You can not modify a list that is not yours')
        else:
            return super(UpdateListView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        listId =self.kwargs['pk']
        return reverse_lazy('view_list', kwargs={'pk': listId})


class ListDeleteView(DeleteView):
    def get_object(self):
        return get_object_or_404(Lista, id= self.kwargs['pk'])

    def get_success_url(self) -> str:
        return reverse('home')


# tasks CRUD

class NewTaskView(View):
    def post(self, request):
        title = request.POST.get('title')
        details = request.POST.get('details')
        periority = request.POST.get('periority')
        lista = Lista.objects.get(id=request.POST.get('pk'))
        if request.is_ajax():
            new_task = Task(title=title,details=details,periority=periority,lista=lista)
            new_task.save()
            return JsonResponse({'done':True}, status=200)
        else:
            return HttpResponse('Go away ya hamada')
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewTaskView, self).dispatch(request, *args, **kwargs)


@login_required
def taskDisplay(request,pk):
    lis= Lista.objects.get(id=pk)
    tasks = Task.objects.filter(lista=lis).order_by('-periority','timing')
    if request.is_ajax():
        x= {'tasks':list(tasks.values())}
        return JsonResponse(x,status=200)
    else:
        return HttpResponse('Go away')


class UpdateTaskView(View):
    def get(self,request,pk):
        edited_task = Task.objects.get(id=pk)
        response={'title':edited_task.title,'details':edited_task.details,'periority':edited_task.periority}
        return JsonResponse(response,status=200)
    def post(self, request,pk):
        title = request.POST.get('title')
        details = request.POST.get('details')
        periority = request.POST.get('periority')
        if request.is_ajax():
            Task.objects.filter(id=pk).update(title=title,details=details,periority=periority)
            return JsonResponse({'done':True}, status=200)
        else:
            return HttpResponse('Go away ya hamada')
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateTaskView, self).dispatch(request, *args, **kwargs)


@login_required
def toggleDone(request, pk):
    if request.is_ajax():
        task= Task.objects.get(id=pk)
        task.done = not task.done
        task.save()
        return JsonResponse({}, status=200)
    else:
        return HttpResponse('Go away')


class DeleteTaskView(DeleteView):
    def get_object(self):
        if not self.request.is_ajax():
            return HttpResponse("Hello there, this isn't your place")
        return get_object_or_404(Task, id= self.kwargs['pk'])

    def get_success_url(self) -> str:
        if self.request.is_ajax():
            return JsonResponse({'done':True},status=200)
        else:
            return HttpResponseNotFound("Hello there, this isn't your place")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteTaskView, self).dispatch(request, *args, **kwargs)
