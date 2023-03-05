from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from groups.forms import CreateGroupForm
from groups.forms import UpdateGroupForm
from groups.forms import GroupFilterForm
from groups.models import Group
from students.models import Student


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'group': group})


class CreateGroupView(CreateView):
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):    # метод будет вызван если форма валидна
        response = super().form_valid(form)
        new_group = form.save()

        students = form.cleaned_data['students']
        for student in students:
            student.group = new_group
            print(student.group)

            if hasattr(student, 'headman_group'):
                group = student.headman_group
                print(group)
                group.headman = None
                group.save()
                print(group)

            student.save()

        return response


class UpdateGroupView(UpdateView):
    model = Group
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            if hasattr(student, 'headman_group'):
                group = student.headman_group
                group.headman = None
                group.save()
            student.save()

        headman_pk = int(form.cleaned_data.get('headman_field'))
        if headman_pk:
            form.instance.headman = Student.objects.get(pk=headman_pk)
        else:
            form.instance.headman = None

        form.save()

        return response


def delete_group(request, pk):
    gr = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        gr.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'group': gr})
