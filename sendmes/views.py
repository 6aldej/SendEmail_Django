from django.shortcuts import render
from .forms import EmailPostForm
from django.core.mail import send_mail

import threading
import time

TASKS = []
NUMBER_OF_TASKS = 10 


def send_mes(request):
    sent = False
    if request.method == 'POST':
        # Форма была отправлена на сохранение.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Все поля формы прошли валидацию.
            cd = form.cleaned_data
            # Отправка электронной почты.
            subject = '{} отправил вам сообщение с задержкой {} секунд'.format(cd['name'], cd['timer'])
            message = '{}'.format(cd['comments'])
            
            timer = cd['timer']
            to = [cd['to']]
            
            TASKS.append({"text": message, "timer": timer})
            t = threading.Timer(timer, send_mail, args=(subject, message, 'gruffbarbecue@gmail.com', to))
            t.start()

            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'send.html', {'form': form, 'sent': sent})

def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:]

def last_tasks(request):
    emails = get_last_tasks()
    return render(request, 'list.html', {'emails': emails})