from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
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


def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})


class DetailCourseView(DetailView):
    model = Course
    # success_url = reverse_lazy('courses:list')
    template_name = 'courses/detail.html'


class CreateCourseView(CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'

# def create_course(request):
#     if request.method == 'GET':
#         form = CreateCourseForm()
#     elif request.method == 'POST':
#         form = CreateCourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#     return render(request, 'courses/create.html', {'form': form})


class UpdateCourseView(UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/delete.html', {'course': course})


class DeleteCourseView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
