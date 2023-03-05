from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from courses.forms import CourseFilterForm, CreateCourseForm, UpdateCourseForm
from courses.models import Course


# Create your views here.
def get_courses(request):
    courses = Course.objects.all()

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'filter_form': filter_form
            }
    )


def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})


# @csrf_exempt
def create_course(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/create.html', {'form': form})


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
