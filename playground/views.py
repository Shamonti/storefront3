from django.conf import settings
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    try:
        print(f'Printing..{settings.BASE_DIR}')
        message = EmailMessage(
            'subject', 'message', 'from@moshbuy.com', ['john@moshbuy.com']
        )
        message.attach_file('playground/static/images/ramadan.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Shamonti'})
