import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.models import PersonModel
from groups.models import Group


class Student(PersonModel):
    # first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first name',
    #                               validators=[MinLengthValidator(3)])
    # last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last name')
    # birthday = models.DateField(default=datetime.date.today)
    # city = models.CharField(max_length=25, null=True, blank=True)
    # email = models.EmailField(validators=[ValidateEmailDomain(*VALID_DOMAINS), validate_unique_email])
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=25, verbose_name='Phone', db_column='phone')

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years


    # @classmethod
    # def generate_fake_data(cls, count):
    #     domain = ('gmail.com', 'yahoo.com', 'test.com')
    #     f = Faker()
    #     groups = Group.objects.all()
    #     for _ in range(count):
    #         s = cls()
    #         s.first_name = f.first_name()
    #         s.last_name = f.last_name()
    #         s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(domain)}'
    #         s.birthday = f.date_between(start_date='-65y', end_date='-18y')
    #         s.phone = f'{f.phone_number()}'
    #         s.group = f.random.choice(groups)
    #         s.save()


    @classmethod
    def _generate(cls):
        f = Faker()
        groups = Group.objects.all()
        students = super()._generate()
        students.phone = f.phone_number()
        students.group = f.random.choice(groups)
        students.save()
