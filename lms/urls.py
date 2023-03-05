from django.contrib import admin
from django.urls import path
from django.urls import include

from core.views import index


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
