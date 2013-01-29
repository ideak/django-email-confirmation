from django.conf import settings

def get_send_mail():
    """
    A function to return a send_mail function suitable for use in the app. It
    deals with incompatibilities between signatures.
    """
    # favour django-mailer but fall back to django.core.mail
    if "mailer" in settings.INSTALLED_APPS:
        from mailer import send_mail
    else:
        from django.core.mail import send_mail as _send_mail
        def send_mail(*args, **kwargs):
            del kwargs["priority"]
            return _send_mail(*args, **kwargs)
    return send_mail

def get_user_model():
    """
    Returns active user model.

    This method is needed for loading custom User models introduced in
    Django 1.5 and backwards compatibility with earlier Django installations.
    """
    try:
        from django.contrib.auth import get_user_model
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        return User
