from django import forms
from django_filters import FilterSet

from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_data',
            'group_description',
        ]

        widgets = {
            'group_start_data': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_data',
            'group_description',
        ]

        widgets = {
            'group_start_data': forms.DateInput(attrs={'type': 'date'})
        }


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['contains'],
            'group_start_data': ['exact']
        }
