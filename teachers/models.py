from random import randint

from django.db import models

from core.models import PersonModel


# Create your models here.
class Teacher(PersonModel):
    # first_name = models.CharField(max_length=50, db_column='First name')
    # last_name = models.CharField(max_length=50, db_column='Last name')
    # birthday = models.DateField(default=datetime.date.today)
    salary = models.PositiveIntegerField(default=10_000)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    def get_salary(self):
        return f'{self.salary}'

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = randint(10_000, 100_000)
        teacher.save()
