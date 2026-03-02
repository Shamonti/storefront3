from django.conf import settings
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        print(f'Printing..{settings.BASE_DIR}')
        message = BaseEmailMessage(
            template_name='emails/hello.html', context={'name': 'Shamonti'}
        )
        message.send(['john@shamonti.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Shamonti'})
