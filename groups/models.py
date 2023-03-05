from django.db import models
from faker import Faker

from core.models import LessonModel
from teachers.models import Teacher


class Group(LessonModel):
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def generate_fake_date(cls):
        f = Faker()
        for _ in 'C#', 'Java', 'PHP', 'Python', 'Ruby', 'Visual Basic', 'C/C++', 'HTML', 'CSS/FIGMA', 'SQL':
            g = cls()
            g.name = _
            g.description = f.sentence()
            g.start_data = f.date_between(start_date='today', end_date='+1y')
            g.clean_fields()
            g.save()
