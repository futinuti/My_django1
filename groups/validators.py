import datetime
from django.core.exceptions import ValidationError


def validate_start_date(date_in):
    if date_in < datetime.date.today():
        raise ValidationError(f'This date "{date_in}" can`t be earlier than date today {datetime.date.today()}')
