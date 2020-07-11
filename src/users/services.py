from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _

from users.models import User, Profile


class AuthenticationService:
    @staticmethod
    def register_new_user(email: str, password: str) -> User:
        """Creates a new user and links it to Profile"""
        email = email.lower() # because Abc@Smth.ru is the same as abc@smth.ru
        exists = get_user_model().objects.filter(username=email)
        if len(exists) != 0:
            raise ValueError(_('user with this email already exists'))
        user = get_user_model().objects.create_user(username=email,
                                                    password=password,
                                                    email=email)
        profile = Profile(user=user)
        profile.save()
        return user

    @staticmethod
    def login_user(email: str, password: str) -> User:
        """Checks the cred pair is OK, returns user if ok"""
        try:
            user = get_user_model().objects.get(username=email.lower())
        except ObjectDoesNotExist:
            raise PermissionError(_('bad email'))
        if not user.check_password(password):
            raise PermissionError(_('bad password'))
        return user

    @staticmethod
    def change_password(user: User, old_password: str, new_password: str) -> User:
        """If old password is ok, change password to the new password, returns user or raises exception"""
        if not user.check_password(old_password):
            raise PermissionError(_('bad password'))
        user.set_password(new_password)
        user.save()
        return user
