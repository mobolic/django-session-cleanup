from celery.task import task
from django.core import management


@task
def cleanup():
    """Cleanup expired sessions by using Django management command."""
    management.call_command("clearsessions", verbosity=0)
