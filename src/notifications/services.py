from django.contrib.auth import get_user_model

from .models import Notification


class NotificationDispatcher:
    """Handles all notifications"""

    def __init__(self, user: get_user_model()):
        self.user = user

    # If you want to notify via some other method — create a function here
    def notify_via_email(self, title, content):
        """Notification via email, creates an internal inactive notification"""
        email = self.user.email
        # notify via email code
        Notification.objects.create_notification(self, title, 'email', content, False)

    def notify_internal(self, title, content):
        Notification.objects.create_notification(self, title, 'internal', content, True)
