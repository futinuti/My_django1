from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView

from teachers.forms import CreateTeacherForm
from teachers.forms import TeacherFilterForm
from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher


# def get_teachers(request):
#     teachers = Teacher.objects.all().order_by('-salary')
#
#     filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)
#
#     return render(
#         request=request,
#         template_name='teachers/list.html',
#         context={'filter_form': filter_form}
#     )


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers = Teacher.objects.all().order_by('-salary')

        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)
        return filter_form


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'title': 'Detail of teacher', 'teacher': teacher})


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


# def create_teacher_view(request):
#     if request.method == 'GET':
#         form = CreateTeacherForm()
#     elif request.method == 'POST':
#         form = CreateTeacherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     return render(request, 'teachers/create.html', {'form': form})


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/delete.html', {'teacher': teacher})


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
