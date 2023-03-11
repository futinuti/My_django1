from django.contrib import admin

from groups.models import Group
from teachers.models import Teacher


# Register your models here.

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


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary')
    list_display_links = list_display
    list_per_page = 15
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthday', 'get_age'),)}),
        ('Contact', {'fields': (('email', 'city'),)}),
        (':-)', {'fields': (('salary',),)})
    )

    def get_age(self, instance):
        return f'{instance.get_age()} year(s)'

    get_age.short_description = 'Age'

    readonly_fields = ('get_age', 'salary')


admin.site.register(Teacher, TeacherAdmin)
