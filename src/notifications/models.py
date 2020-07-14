from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from django.db import models


class NotificationManager(models.Manager):
    def unread(self):
        return self.filter(read=True)

    def active(self):
        return self.filter(active=True)

    def actual(self):
        """Active, Unread and up to date"""
        active = self.filter(active=True)
        unread = active.filter(unread=True)
        return unread.filter(lambda x: x.created_date > datetime.now)

    def create_notification(self, user: get_user_model(), title: str, type: str, content: str = "", active=False):
        """Create and save a notification with the given type, and content."""
        if not title or not type:
            raise ValueError('You should provide type and title')
        if type not in self.get_notification_types_list():
            raise ValueError('Provided type is not available')
        notification = self.model(
            title=title,
            type=type,
            content=content,
            active=active,
            read=False
        )
        notification.save()
        return notification


class Notification(models.Model):
    """Holds any notifications"""
    NOTIFICATION_TYPES = (
        ('email', _('Email notification')),
        ('internal', _('Internal_notification'))
    )

    user = models.ForeignKey(to=get_user_model(), verbose_name=_('User'), on_delete=models.CASCADE)
    type = models.CharField(verbose_name=_('Notification type'), choices=NOTIFICATION_TYPES)
    title = models.CharField(verbose_name=_('Notification title'), max_length=512)
    content = models.TextField(verbose_name=_('Notification content'), max_length=2048, blank=True)

    created_date = models.DateTimeField(auto_created=True, default=datetime.now)
    active = models.BooleanField(verbose_name=_('Notification is active'))
    read = models.BooleanField(verbose_name=_('Notification is read'))

    objects = NotificationManager()

    def get_notification_types_list(self) -> list:
        """Get all notification types in list format e.g check if provided type is supported"""
        result = []
        for t in self.NOTIFICATION_TYPES:
            result.append(t[0])
        return result

    def __str__(self):
        return self.title + ' ' + self.created_date.isoformat()
