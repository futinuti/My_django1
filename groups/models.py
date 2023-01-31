from django.db import models
import datetime
from faker import Faker
from groups.validators import validate_start_date


LANG_LIST = ('C++/CLI', 'C#', 'Object Pascal', 'Java', 'Perl', 'PHP', 'Python', 'Ruby', 'Visual Basic')


class Group(models.Model):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='G_name')
    group_start_data = models.DateField(default='2023-06-24', validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name} {self.group_start_data}'

    @classmethod
    def generate_fake_date(cls, count):
        f = Faker()
        for _ in range(count):
            g = cls()
            g.group_name = f.random.choice(LANG_LIST)
            g.group_description = f.sentence()
            g.group_start_data = f.date_between(start_date='today', end_date='+1y')
            g.clean_fields()
            g.save()
