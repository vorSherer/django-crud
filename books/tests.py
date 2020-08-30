from django.test import TestCase
from django.urls import reverse


class BooksTest(TestCase):

    # Helper functions *****************************

    def helper_page_status_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def helper_page_templates_used(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, f'{url_name}.html')
    

    # Unit Tests *****************************
    
    def test_home_page_status_pass(self):
        self.helper_page_status_200('home')

    def test_home_page_templates_used(self):
        self.helper_page_templates_used('home')

    