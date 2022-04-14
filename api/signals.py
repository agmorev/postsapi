
from django.utils import timezone
from django.core.signals import request_finished, request_started
from django.dispatch import receiver

from rest_framework_simplejwt.tokens import AccessToken

from users.models import User


# @receiver(request_started)
# def api_request_signal(sender, environ, **kwargs):
#     print('Request started')
#     print("Sender:", sender)
#     print("Environ:", environ)
#     print("Kwargs:", kwargs)
    
#     token = environ['HTTP_AUTHORIZATION'][7:]
#     access_token = AccessToken(token)
#     user = User.objects.get(id=access_token['user_id'])
#     user.last_login = timezone.now()
#     user.save(update_fields=["last_login"])
    
    
   

# @receiver(request_finished)
# def post_request(sender, *args, **kwargs):
#     pass