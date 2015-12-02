from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import BadHeaderError, send_mail
from .models import UserProfile


def user_login_check(user):
    return user.is_anonymous()


@user_passes_test(user_login_check)
def create_account(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date = request.POST['date']
        sex = request.POST['sex']
        user = User.objects.filter(username=username).first()
        user1 = User.objects.filter(email=email).first()
        if user is None and user1 is None:
            profile = UserProfile()
            profile.born_date = date
            profile.sex = sex
            profile.user = User(username=username, password=password, email=email, first_name=name, last_name=last_name)
            profile.save()
            return redirect(reverse('account:dashboard'))
        else:
            sms = "Ese nombre de usuario ya esta siendo usado por otro, por favor seleccione otro"
            error = True
        return render(request, 'create_account.html', locals())
    else:
        return render(request, 'create_account.html', locals())


@login_required
def user_search(request):
    pass


@login_required
def user_update(request, pk):
    profile = UserProfile.objects.get(user_id=pk)
    return render(request, 'edit_profile.html', locals())


def friendship(request):
    pass


def user_profile(request, pk):
    profile = UserProfile.objects.get(user_id=pk)
    own = UserProfile.objects.get(pk=request.user.pk)
    is_my_profile = own == profile
    return render(request, 'user_profile.html', locals())


@login_required
def user_login(request):
    users = UserProfile.objects.filter(is_conected=True).exclude(user_id=request.user.pk)
    return render(request, 'user_login.html', locals())


@login_required
def user_staff_login(request):
    users_staff = UserProfile.objects.filter(is_conected=True, user__is_staff=True).exclude(user_id=request.user.pk)
    return render(request, 'user_staff.html', locals())


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


def information(request):
    mesagge = 'Informaciones recientes'
    return render(request, 'informations.html', locals())


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
    profile = UserProfile.objects.get(user_id=request.user.pk)
    return render(request, 'contact.html', locals())


def terms(request):
    return render(request, 'terms.html')


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')
