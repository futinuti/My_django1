from django import forms
from django_filters import FilterSet

from teachers.models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'salary',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'salary',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['contains'],
            'last_name': ['contains']
        }
