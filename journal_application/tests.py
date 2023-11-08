from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
# Create your tests here.

class Notebook(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_create_notebook(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Notebook', self.browser.title)
        self.fail('Finish the test!')
