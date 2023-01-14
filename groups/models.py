from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='G_name')
    start_data_group = models.DateField(default='2023-06-24')
    group_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'
