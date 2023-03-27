from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x 
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