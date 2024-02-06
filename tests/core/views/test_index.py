from django.test import TestCase

from django.urls import reverse


class IndexViewTestCase(TestCase):
    def test_index_view_status_code(self):
        # Make a GET request to the IndexView using the test client
        response = self.client.get(reverse('index'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        # Make a GET request to the IndexView using the test client
        response = self.client.get(reverse('index'))

        # Check if the correct template is used in the response
        self.assertTemplateUsed(response, 'core/Index.html')
