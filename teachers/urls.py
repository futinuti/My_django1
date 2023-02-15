from django.contrib import admin
from django.urls import path

from groups.views import get_groups
from groups.views import detail_group
from groups.views import update_group
from groups.views import create_group_view
from students.views import get_students
from students.views import delete_student
from students.views import create_student_view
from students.views import update_student
from students.views import detail_student
from students.views import index
from teachers.views import get_teachers
from teachers.views import create_teacher_view
from teachers.views import update_teacher
from teachers.views import detail_teacher


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', get_students, name='list_students'),
    path('teachers/', get_teachers),
    path('groups/', get_groups),
    path('students/create/', create_student_view, name='create_students'),
    path('teachers/create/', create_teacher_view),
    path('groups/create/', create_group_view),
    path('students/update/<int:pk>/', update_student, name='update_students'),
    path('teachers/update/<int:pk>/', update_teacher),
    path('groups/update/<int:pk>/', update_group),
    path('students/detail/<int:pk>/', detail_student, name='detail_students'),
    path('teachers/detail/<int:pk>/', detail_teacher),
    path('groups/detail/<int:pk>/', detail_group),
    path('students/delete/<int:pk>/', delete_student, name='delete_students')
]
