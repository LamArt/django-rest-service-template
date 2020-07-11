from django.test import TestCase

from .services import AuthenticationService
from .models import Profile, User


class AuthenticationServiceTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user('test@test.ru', 'test@test.ru', '1234')

    def test_register_user_creates_profile(self) -> None:
        """register_user_creates_profile"""
        u = AuthenticationService.register_new_user('buddy@club.ru', '1234')
        profile_QS = Profile.objects.filter(user=u)
        self.assertEqual(len(profile_QS), 1)

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

    def test_password_change_with_correct_credentials(self) -> None:
        """Change password, try to login with new creds"""
        source_u = User.objects.get(username='test@test.ru')
        AuthenticationService.change_password(source_u, '1234', '12345')
        u = AuthenticationService.login_user('test@test.ru', '12345')
        self.assertEqual(u, source_u)

    def test_password_change_with_incorrect_credentials(self) -> None:
        """Change password with bad creds, try to login with bad creds"""
        source_u = User.objects.get(username='test@test.ru')
        self.assertRaises(PermissionError, lambda: AuthenticationService.change_password(source_u, '123', '12345'))
        AuthenticationService.change_password(source_u, '1234', '12345')
        self.assertRaises(PermissionError, lambda: AuthenticationService.login_user('test@test.ru', '1234'))
