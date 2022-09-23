from django.db import models

from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name="invitations_received",
        on_delete=models.CASCADE,
        verbose_name="User to invite",
        help_text="Please select the user you want to invite."
    )

    message = models.CharField(
        max_length=300, blank=True,
        verbose_name="Optional Message",
        help_text="It's always nice to add a message!")
