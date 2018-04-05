import datetime
from importlib import import_module

from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone

from session_cleanup.tasks import cleanup


class CleanupTest(TestCase):
    @override_settings(SESSION_ENGINE="django.contrib.sessions.backends.file")
    @override_settings(SESSION_SERIALIZER="django.contrib.sessions.serializers.PickleSerializer")   # noqa: E501
    def test_session_cleanup(self):
        """
        Tests that sessions are deleted by the task
        """
        engine = import_module(settings.SESSION_ENGINE)
        SessionStore = engine.SessionStore

        now = timezone.now()
        last_week = now - datetime.timedelta(days=7)
        stores = []
        unexpired_stores = []
        expired_stores = []

        # create unexpired sessions
        for i in range(20):
            store = SessionStore()
            store.save()
            stores.append(store)

        for store in stores:
            self.assertEqual(store.exists(store.session_key), True,
                             "Session store could not be created.")

        unexpired_stores = stores[:10]
        expired_stores = stores[10:]

        # expire some sessions
        for store in expired_stores:
            store.set_expiry(last_week)
            store.save()

        cleanup()

        for store in unexpired_stores:
            self.assertEqual(store.exists(store.session_key), True,
                             "Unexpired session was deleted by cleanup.")

        for store in expired_stores:
            self.assertEqual(store.exists(store.session_key), False,
                             "Expired session was not deleted by cleanup.")
