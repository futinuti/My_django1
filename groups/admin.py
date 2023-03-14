from django import forms
from django.contrib import admin

from groups.models import Group
from teachers.models import Teacher


class TeachersInLine(admin.TabularInline):
    model = Group.teachers.through

    fields = ('get_first_name', 'get_last_name', 'get_salary')
    exclude = ('teachers', )
    extra = 0
    readonly_fields = fields

    def get_first_name(self, instance):
        return f'{Teacher.objects.get(pk=instance.pk).get_first_name()}'

    def get_last_name(self, instance):
        return f'{Teacher.objects.get(pk=instance.pk).get_last_name()}'

    def get_salary(self, instance):
        return f'{Teacher.objects.get(pk=instance.pk).get_salary()}'

    get_first_name.short_description = 'first_name'
    get_last_name.short_description = 'last_name'
    get_salary.short_description = 'salary'

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False




class StudentsInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = fields
    # show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].choices = [(s.pk, f'{s.first_name} {s.last_name}') for s in self.instance.students.all()]
        self.fields['headman'].choices.insert(0, (0, '====='))

        self.fields['headman'].widget.can_add_related = False
        self.fields['headman'].widget.can_change_related = False
        self.fields['headman'].widget.can_view_related = False
        self.fields['headman'].widget.can_delete_related = False

    class Meta:
        model = Group
        fields = '__all__'


# @admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ('name', 'start_data')
    fields = (
        'name',
        'start_data',
        'headman',
        # 'teachers',
        ('created', 'updated'),
    )

    readonly_fields = ('created', 'updated')
    inlines = [StudentsInlineTable, TeachersInLine]
    exclude = ('teachers',)


admin.site.register(Group, GroupAdmin)
