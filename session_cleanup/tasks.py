from celery.task import task
from django.core import management


@task
def cleanup():
    """
    Cleanup expired sessions by using Django management command.

    Since the command's name changed in Django 1.5, we must try using
    both 'clearsessions' and 'cleanup'.

    """
    try:
        management.call_command("clearsessions", verbosity=0)
    except management.base.CommandError:
        management.call_command("cleanup", verbosity=0)
