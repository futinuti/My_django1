from django import forms

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
