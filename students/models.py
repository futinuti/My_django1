
from django.db import models
from django.db.models.signals import pre_init, post_save, pre_save, post_init
from django.dispatch import receiver
from faker import Faker

from core.models import PersonModel
from groups.models import Group


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    phone = models.CharField(max_length=25, verbose_name='Phone', db_column='phone')

    class Meta:
        db_table = 'students'

    def __str__(self):
        if self.group:
            return f'{self.first_name} {self.last_name} {self.group.name}'
        else:
            return f'{self.first_name} {self.last_name} ( )'

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


@receiver(pre_init, sender=Student)
def pre_init_signal(sender, **kwargs):
    print(f'PRE INIT: {kwargs}')


@receiver(post_init, sender=Student)
def post_init_signal(sender, **kwargs):
    print(f'POST INIT: {kwargs}')


@receiver(pre_save, sender=Student)
def pre_save_signal(sender, **kwargs):
    print(f'PRE SAVE: {kwargs}')


@receiver(post_save, sender=Student)
def post_save_signal(sender, **kwargs):
    print(f'POST SAVE: {kwargs}')