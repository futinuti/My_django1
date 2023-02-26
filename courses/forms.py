from django import forms
from django_filters import FilterSet

from courses.models import Course


class CourseBaseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_data': forms.DateInput(attrs={'type': 'date'})
        }


class CreateCourseForm(CourseBaseForm):

    class Meta(CourseBaseForm.Meta):
        pass


class UpdateCourseForm(CourseBaseForm):

    class Meta(CourseBaseForm.Meta):
        exclude = [
            'start_data',
            'description'
        ]


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['contains'],
            'start_data': ['exact']
        }
