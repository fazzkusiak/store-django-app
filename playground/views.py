from django.core.cache import cache
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from store.tasks import notify_customers
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import logging


logger = logging.getLogger(__name__) 
# Create your views here.
class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.crticial('httpbin is offline')
        return render(request, 'hello.html', {'name' : data})

# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name' : data})

'''
def say_hello(request):
    try:        
        send_mail('subject', 'message', 'info@test.com', ['test@test.com'])
        
        mail_admins('subject', 'message', html_message='message')
        
        message = EmailMessage('subject', 'test@test.com', 'test@test.com', ['test2@test.com', 'test3@test.com'])
        message.attach_file('playground/static/images/xcvxcvxcv.png')
        message.send()

        message = BaseEmailMessage(
            template_name="emails/hello.html",
            context={'name': 'real_nombre'}
        )
        message.send(['test@test.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name' : 'Mosh'})
'''