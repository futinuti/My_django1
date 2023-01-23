from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
        ]
        # fields = '__all__'
        # exclude = []
    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

