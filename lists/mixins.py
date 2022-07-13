from django.http import JsonResponse

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response
        
        

# class UpdateTaskView(UpdateView):
#     form_class = TaskForm
#     template_name = 'lists/update_task.html'
#     # success_url = '/'
#     model = Task
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(UpdateTaskView, self).dispatch(request, *args, **kwargs)


# class TaskView(View):

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         lis= Lista.objects.get(id=self.kwargs['pk'])
#         context['tasks'] = Task.objects.filter(lista=lis).order_by('-periority','timing')
#         return context

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(TaskView, self).dispatch(request, *args, **kwargs)

#     def get(request):
#         # ctx={}
#         lis= Lista.objects.get(id=request.GET.get('pk'))
#         # print(self.kwargs)
#         tasks = Task.objects.filter(lista=lis).order_by('-periority','timing')
#         # if request.is_ajax:
#         return JsonResponse({'tasks':list(tasks.values())})
#         # else:
#         #     pass

