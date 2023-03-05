from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from groups.forms import CreateGroupForm, GroupFilterForm
from groups.forms import UpdateGroupForm
from groups.models import Group
from students.models import Student


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'

    def get_queryset(self):
        groups = Group.objects.all()

        filter_form = GroupFilterForm(data=self.request.GET, queryset=groups)
        return filter_form

# def detail_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     return render(request, 'groups/detail.html', {'group': group})


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


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'


class DetailGroupView(DetailView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/detail.html'

