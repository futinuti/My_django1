from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from groups.forms import CreateGroupForm
from groups.forms import UpdateGroupForm
from groups.forms import GroupFilterForm
from groups.models import Group
from students.models import Student


def get_groups(request):
    groups = Group.objects.all().order_by('group_start_data')

    filter_form = GroupFilterForm(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={'filter_form': filter_form}
    )


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'title': 'Detail of group', 'group': group})


# @csrf_exempt
def create_group_view(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group, initial=students)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    gr = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        gr.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'group': gr})
