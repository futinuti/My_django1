from django.contrib import admin
from django.urls import path
from students.views import get_students, create_student_view, update_student, detail_student
from students.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student)
]
