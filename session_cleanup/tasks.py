from celery import shared_task
from django.core import management


@shared_task
def cleanup():
    """Cleanup expired sessions by using Django management command."""
    management.call_command("clearsessions", verbosity=0)
