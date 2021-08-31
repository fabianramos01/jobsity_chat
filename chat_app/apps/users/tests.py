from django.test import TestCase, Client

from selenium.webdriver import Firefox

from apps.users.models import CustomUser

class TestUsers(TestCase):

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        CustomUser.objects.create_user(username='Jose', password='X9YNyH17A234v')

    def test_create_user(self):
        response = self.client.post('/register', {'username': 'Carlos', 'password1': 'X9YNyH17A9!b', 'password2': 'X9YNyH17A9!b'})
        self.assertEqual(response.status_code, 302)

    def test_login_user(self):
        response = self.client.post('/', {'username': 'Jose', 'password1': 'X9YNyH17A234v'})
        print(response.get_host())
        self.assertEqual(response.status_code, 302)
