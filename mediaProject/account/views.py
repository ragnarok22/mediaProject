from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from .models import UserProfile


def create_account(request):
    if request.method == 'POST':
        return render(request, 'create_account.html', locals())
    else:
        return render(request, 'create_account.html', locals())


@login_required
def user_search(request):
    pass


@login_required
def user_update(request):
    pass


def friendship(request):
    pass


@login_required
def user_login(request):
    users = UserProfile.objects.filter(is_conected=True)
    return render(request, 'user_login.html', locals())


@login_required
def dashboard(request):
    if request.method == 'GET':
        users = UserProfile.objects.filter(is_conected=True)
        user = request.user
        return render(request, 'index.html', locals())
    else:
        email = request.POST.get('email', "")
        subject = request.POST.get('subject', "")
        message = request.POST.get('message', "")
        if email and subject and message:
            try:
                # email = EmailMultiAlternatives(subject, message, 'rhernandeza@facinf.uho.edu.cu',
                # ['rhernandeza@facinf.uho.edu.cu'])
                # message_html = '<h1>' + message + '</h1>'
                # email.attach_alternative(message_html, 'text/html')
                # email.send(False)
                subject = '[The Wall] ' + subject
                send_mail(subject, message, 'rhernandeza@facinf.uho.edu.cu', ['rhernandeza@facinf.uho.edu.cu'], False,
                          'rhernandeza', 'seabiskuit32+')
            except BadHeaderError:
                error = True
                message_error = 'Se ha encontrado una cabecera invalida'
                return render(request, 'index.html', locals())
            return render(request, 'index.html', locals())
        else:
            error = True
            message_error = 'Debe de llenar todos los campos'
            return render(request, 'index.html', locals())


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('account:dashboard'))
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is None:
                error = True
                message = 'Usuario o contrasena incorrectos'
                return render(request, 'login.html', locals())
            elif user.is_active:
                login(request, user)
                profile = UserProfile.objects.get(user=user)
                profile.is_conected = True
                profile.save()
                return redirect(reverse('account:dashboard'))
            else:
                error = True
                message = 'Este usuario ha sido baneado, por favor contacte al administrador'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())


@login_required
def logout_view(request):
    profile = UserProfile.objects.get(user=request.user)
    profile.is_conected = False
    profile.save()
    logout(request)
    return redirect(reverse('account:login'))


def contact_us(request):
    return render(request, 'contact.html')


def terms(request):
    return render(request, 'terms.html')


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')
