import datetime


def strftime_slurm(dt: datetime.datetime):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


def now():
    return datetime.datetime.now()


def today():
    return datetime.today()


def last_month_som():
    """First second of previous month.
    """
    return (
        now().replace(day=1) - datetime.timedelta(days=1)
    ).replace(day=1, hour=0, minute=0, second=0)


def last_month_eom():
    """Last second of previous month.
    """
    return (
        now().replace(day=1) - datetime.timedelta(days=1)
    ).replace(hour=23, minute=59, second=59)
