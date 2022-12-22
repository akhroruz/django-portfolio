from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView

from apps.forms import MessageForm
from apps.models import Project, Skill, Category


class MessageView(FormView, ListView):
    template_name = 'apps/index.html'
    form_class = MessageForm
    success_url = reverse_lazy('index')
    queryset = Project.objects.all()
    context_object_name = 'projects'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CustomDetailView(DetailView):
    template_name = 'apps/portfolio-details.html'
    queryset = Project.objects.all()
    context_object_name = 'project'
