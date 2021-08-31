from django.test import TestCase, Client

class TestUrlAccess(TestCase):

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_access_login_with_user_logged(self):
        response = self.client.post('/chat/jobsity')
        self.assertEqual(response.status_code, 301)