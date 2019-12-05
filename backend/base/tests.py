from django.test import TestCase
from base.models import City, State


class StateTestCase(TestCase):
    def setUp(self):
        State.objects.create(initials='PB')

    def test_state_exists(self):
        """Validate simple add of a State"""
        pb = State.objects.get(initials='PB')

        self.assertEqual(str(pb), 'PB')
