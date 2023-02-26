from django.urls import path

from courses.views import get_courses, create_course, UpdateCourseView, detail_course, delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_course, name='detail'),
    path('delete/<int:pk>/', delete_course, name='delete'),
]
