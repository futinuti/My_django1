from django.contrib import admin
from django.urls import path
from django.urls import include

from core.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),
]
