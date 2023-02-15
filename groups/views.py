from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.fields import Str
from webargs.djangoparser import use_args

from groups.forms import CreateGroupForm, UpdateGroupForm
from groups.models import Group


@use_args(
    {
        'group_name': Str(required=False),
        'group_start_data': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all().order_by('group_start_data')

    if len(args) and (args.get('group_name') or args.get('group_start_data')):
        groups = groups.filter(
            Q(group_name=args.get('group_name', '')) | Q(group_start_data=args.get('group_start_data', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={'title': 'List of groups', 'groups': groups}
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
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, pk):
    gr = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        gr.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'group': gr})
