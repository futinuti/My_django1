from django.db import models

from core.models import BaseModel, LessonModel


# Create your models here.
class Course(LessonModel):
    groups_link = models.OneToOneField(
        'groups.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='group_link')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.name}'
