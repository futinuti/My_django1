from django.urls import path

from courses.views import UpdateCourseView
from courses.views import ListCourseView
from courses.views import DetailCourseView
from courses.views import CreateCourseView
from courses.views import DeleteCourseView

app_name = 'courses'

urlpatterns = [
    path('', ListCourseView.as_view(), name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
]
