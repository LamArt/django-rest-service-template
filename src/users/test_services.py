from django.test import TestCase

from .services import AuthenticationService
from .models import Profile, User


class AuthenticationServiceTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user('test@test.ru', 'test@test.ru', '1234')

    def test_register_user_creates_profile(self) -> None:
        """register_user_creates_profile"""
        u = AuthenticationService.register_new_user('buddy@club.ru', '1234')
        profileQS = Profile.objects.filter(user=u)
        self.assertEqual(len(profileQS), 1)

    def test_register_user_validators(self) -> None:
        """Can't register existing"""
        self.assertRaises(ValueError, lambda: AuthenticationService.register_new_user('test@test.ru', '1234'))

    def test_email_with_correct_creds_login(self) -> None:
        """Abc@abC.ru should eq abc@abc.ru"""
        source_u = User.objects.get(username='test@test.ru')
        u = AuthenticationService.login_user('Test@test.ru', '1234')
        u2 = AuthenticationService.login_user('test@Test.ru', '1234')
        u3 = AuthenticationService.login_user('test@test.ru', '1234')
        self.assertEqual(u, source_u)
        self.assertEqual(u2, source_u)
        self.assertEqual(u3, source_u)

    def test_email_with_incorrect_creds_login(self) -> None:
        """Not correct pass | Not correct email"""
        self.assertRaises(PermissionError, lambda:  AuthenticationService.login_user('Tost@test.ru', '1234'))
        self.assertRaises(PermissionError, lambda:  AuthenticationService.login_user('Test@test.ru', '12345'))
