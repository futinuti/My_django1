from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView

from teachers.forms import CreateTeacherForm
from teachers.forms import TeacherFilterForm
from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers = Teacher.objects.all().order_by('-salary')

        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)
        return filter_form


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
