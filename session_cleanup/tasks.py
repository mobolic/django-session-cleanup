from celery.task import task
from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.cache import cache
from django.utils.importlib import import_module


import datetime


@task
def cleanup():
    engine = import_module(settings.SESSION_ENGINE)
    SessionStore = engine.SessionStore

    expired_sessions = Session.objects.filter(expire_date__lte=datetime.datetime.now())

    for session in expired_sessions:
        store = SessionStore(session.session_key)
        store.delete()
