import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from students.validators import ValidateEmailDomain, validate_unique_email


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    domain = ('gmail.com', 'yahoo.com', 'test.com')
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last name')
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*domain), validate_unique_email])

    class Meta:
        abstract = True

    def get_first_name(self):
        return f'{self.first_name}'

    def get_last_name(self):
        return f'{self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-18y'),
            email=f'{first_name}.{last_name}@{f.random.choice(cls.domain)}',
            city=f.city()
        )
        obj.save()

        return obj


    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()


class LessonModel(BaseModel):
    name = models.CharField(max_length=80, verbose_name='name', db_column='name')
    start_data = models.DateField(default='2023-06-24')
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
