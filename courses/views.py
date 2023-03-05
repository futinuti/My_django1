from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView

from courses.forms import CourseFilterForm, CreateCourseForm, UpdateCourseForm
from courses.models import Course


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_queryset(self):
        courses = Course.objects.all()

        filter_form = CourseFilterForm(data=self.request.GET, queryset=courses)
        return filter_form


class DetailCourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
