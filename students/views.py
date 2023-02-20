from django.db.models import Q
from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str
from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
# )
def get_students(request):
    students = Student.objects.all().order_by('birthday')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'filter_form': filter_form
            }
    )


def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'title': 'Detail of student', 'student': student})


# @csrf_exempt
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/create.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/update.html', {'form': form})


def delete_student(request, pk):
    st = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': st})
