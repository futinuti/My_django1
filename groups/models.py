from django.db import models
from faker import Faker

from core.models import BaseModel
from groups.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='G_name')
    group_start_data = models.DateField(default='2023-06-24', validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name} {self.group_start_data}'

    @classmethod
    def generate_fake_date(cls):
        f = Faker()
        for _ in 'C#', 'Java', 'PHP', 'Python', 'Ruby', 'Visual Basic', 'C/C++', 'HTML', 'CSS/FIGMA', 'SQL':
            g = cls()
            g.group_name = _
            g.group_description = f.sentence()
            g.group_start_data = f.date_between(start_date='today', end_date='+1y')
            g.clean_fields()
            g.save()
