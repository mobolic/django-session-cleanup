======================
Django Session Cleanup
======================

For projects that use the ``cached_db`` or ``db`` session engines, the
``django_session`` table can get quite large after a while.

Django provides the 'cleanup' management command for deleting expired sessions
from this table but you have to either run this command manually or
set-up a cron job.

Django Session Cleanup provides a periodic task for
`Celery <http://celeryproject.org/>`_ that will delete expired sessions.

Usage
-----

1. Run ``pip install django-session-cleanup``.

2. Add ``session_cleanup`` to ``INSTALLED_APPS`` in your project's settings.

3. Edit or create ``CELERYBEAT_SCHEDULE`` in your project's settings::

    from session_cleanup.settings import weekly_schedule
    CELERYBEAT_SCHEDULE = {
        ...
        'session_cleanup': weekly_schedule
    }
