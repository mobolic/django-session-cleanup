

from celery.schedules import crontab

weekly_schedule = {
    'task': 'session_cleanup.tasks.cleanup',
    'schedule': crontab(hour=0, minute=0, day_of_week="sunday"),
}

nightly_schedule = {
    'task': 'session_cleanup.tasks.cleanup',
    'schedule': crontab(hour=0, minute=0),
}
