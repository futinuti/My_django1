import datetime

from django.db import models
from faker import Faker


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, db_column='First name')
    last_name = models.CharField(max_length=50, db_column='Last name')
    birthday = models.DateField(default=datetime.date.today)
    salary = models.PositiveIntegerField()

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday} {self.salary}'

    @classmethod
    def generate_fake_data(cls, count):
        f = Faker()
        for _ in range(count):
            s = cls()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.birthday = f.date_between(start_date='-65y', end_date='-29y')
            s.salary = f.random.randint(15000, 150000)
            s.save()
