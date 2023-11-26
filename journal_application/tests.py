from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.urls import reverse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from django.test import TestCase
from .models import Notebook, Journal

# Unit Tests
class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword') 

class NotebookModelTest(TestCase):    
    def test_notebook_creation(self):
        testuser = User.objects.create(username='testuser2', password='testpassword2')
        notebook = Notebook.objects.create(user=testuser, title='My Notebook')
        self.assertEqual(notebook.title, 'My Notebook')

class JournalModelTest(TestCase):
    def test_journal_creation(self):
        testuser = User.objects.create(username='testuser3', password='testpassword3')
        notebook = Notebook.objects.create(user=testuser, title='My Notebook2')
        journal = Journal.objects.create(notebook=notebook, title='My Journal Entry', content='Sample content')
        self.assertEqual(journal.title, 'My Journal Entry')
        self.assertEqual(journal.notebook, notebook)


class NotebookSeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        User.objects.create_user(username='testuser', password='testpassword')
        self.login()

    def login(self):
        self.driver.get(f'{self.live_server_url}{reverse("login")}')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_username'))
        )
        username_input = self.driver.find_element(By.ID, 'id_username')
        username_input.send_keys('testuser')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_password'))
        )
        password_input = self.driver.find_element(By.ID, 'id_password')
        password_input.send_keys('testpassword')
        password_input.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.live_server_url + reverse('index')))

    def create_notebook(self):
        self.driver.get(f'{self.live_server_url}{reverse("create_notebook")}')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_title'))
        )
        title_input = self.driver.find_element(By.ID, 'id_title')
        title_input.send_keys('My New Notebook')
        about_input = self.driver.find_element(By.ID, 'id_about')
        about_input.send_keys('This is a test notebook.')
        self.driver.find_element(By.ID, 'submit').click()
        
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.live_server_url + reverse('index')))
