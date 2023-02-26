from django.urls import path

from .views import get_teachers
from .views import delete_teacher
from .views import create_teacher_view
from .views import UpdateTeacherView
from .views import detail_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher_view, name='create'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail'),
    path('delete/<int:pk>/', delete_teacher, name='delete')
]
