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
            'phone',
        ]
        # fields = '__all__'
        # exclude = []

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        # убираем лишние символы
        # cleaned_phone = ''.join([i for i in value if i.isdigit() or i in ['-', '+', '(', ')']])

        cleaned_phone = ''.join([i for i in value if i.isdigit()])
        kod_country = cleaned_phone[:-10:1]
        cleaned_phone = f'+{kod_country} ({cleaned_phone[-10:-7:1]}) {cleaned_phone[-7:-4:1]}-' \
                        f'{cleaned_phone[-4:-2:1]}-{cleaned_phone[-2::1]}'
        return cleaned_phone
