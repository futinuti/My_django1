from django.urls import path

from .views import get_groups
from .views import delete_group
from .views import detail_group
from .views import update_group
from .views import CreateGroupView

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    # path('create/', create_group_view, name='create'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('update/<int:pk>/', update_group, name='update'),
    path('detail/<int:pk>/', detail_group, name='detail'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]
