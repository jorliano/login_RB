from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    messages.info(request, 'Seja benvindo %s' % user.username)
