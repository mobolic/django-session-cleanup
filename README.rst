======================
Django Session Cleanup
======================

A periodic task for removing expired Django sessions from the django_session table

For projects that use the ``django.contrib.sessions.backends.cached_db`` or ``django.contrib.sessions.backends.db`` session engines, the ``django_session`` table can get quite large after a while.  Django provides the 'cleanup' management command for deleting expired sessions from this table but you have to either run this command manually or set-up a cron job.  Django Session Cleanup provides a periodic task for `Celery <http://celeryproject.org/>`_ that will delete expired sessions on a weekly basis.

Usage
-----

1. Run ``python setup.py install`` to install,
   or place ``session_cleanup`` on your Python path.

2. Add ``session_cleanup`` to your list of ``INSTALLED_APPS``.

3. Add an entry to, or create a ``CELERYBEAT_SCHEDULE`` in your project's settings::

    from session_cleanup.settings import weekly_schedule
    CELERYBEAT_SCHEDULE = {
        ...
        'session_cleanup': weekly_schedule
    }

