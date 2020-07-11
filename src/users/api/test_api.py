from rest_framework.test import APITestCase
from rest_framework.utils import json

from users.models import User


class APITests(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user('test@test.ru', 'test@test.ru', '1234')

    def test_register_login_with_correct_credentials(self) -> None:
        """register_user_creates_profile -> login to the system"""
        response = self.client.post('/account/register/',
                                    json.dumps({'email': 'ivan@foo.bar', 'password': '1234'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/account/login/',
                                    json.dumps({'email': 'ivan@foo.bar', 'password': '1234'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_register_with_incorrect_credentials(self) -> None:
        """register with bad email or with email, that already is in the system"""
        response = self.client.post('/account/register/',
                                    json.dumps({'email': 'totally_accurate_email_address', 'password': '1234'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/account/register/',
                                    json.dumps({'email': 'test@test.ru', 'password': '1234'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_with_incorrect_credentials(self) -> None:
        """login with bad email or with bad password"""
        response = self.client.post('/account/login/',
                                    json.dumps({'email': 'why_am_i_alive', 'password': '1234'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/account/login/',
                                    json.dumps({'email': 'test@test.ru', 'password': '12345'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403)
