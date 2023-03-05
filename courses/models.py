from django.db import models

from core.models import BaseModel, LessonModel


# Create your models here.
class Course(LessonModel):
    # name = models.CharField(max_length=80, verbose_name='Name', db_column='Name')
    # start_data = models.DateField(default='2023-06-24')
    # description = models.TextField(null=True, blank=True)
    groups_link = models.OneToOneField(
        'groups.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='group_link')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.name} {self.start_data}'
