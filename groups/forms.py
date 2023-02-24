from django import forms
from django_filters import FilterSet

from groups.models import Group
from students.models import Student


class GroupBaseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def save(self, commit=True):
        new_group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_start_data': forms.DateInput(attrs={'type': 'date'})
        }

class CreateGroupForm(GroupBaseForm):
    # дополнительное поле со списком студентов. множественный выбор с контр
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False)  # все студенты
    # # students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True))  # студенты без групп
    # # '''
    # # SELECT *
    # # FROM student
    # # WHERE group is null;
    # # '''
    # def save(self, commit=True):
    #     new_group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = new_group
    #         student.save()
    #
    # class Meta:
    #     model = Group
    #     fields = '__all__'
    #
    #     widgets = {
    #         'group_start_data': forms.DateInput(attrs={'type': 'date'})
    #     }
    # переопределить конструктор
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all().select_related('group')
    # filter(group__isnull=True)

    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False)
    #
    # def save(self, commit=True):
    #     new_group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = new_group
    #         student.save()
    # выполнить начальную инициализацию этого поля

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all().select_related('group')

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_data',
            'group_description'
        ]
        # model = Group
        # fields = [
        #     'group_name',
        #     'group_start_data',
        #     'group_description',
        # ]
        #
        # widgets = {
        #     'group_start_data': forms.DateInput(attrs={'type': 'date'})
        # }



class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['contains'],
            'group_start_data': ['exact']
        }
