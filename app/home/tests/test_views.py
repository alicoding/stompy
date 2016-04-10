from django.core.urlresolvers import reverse
from django.test import TestCase


class TestLandingView(TestCase):

    def test_view_returns_200(self):
        response = self.client.get(reverse('home.landing'))
        self.assertEqual(response.status_code, 200)
