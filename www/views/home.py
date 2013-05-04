from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
import smtplib

def index(request):
    # /
    return render_to_response('www/home.html', {}, RequestContext(request))

def about(request):
    # about/
    return render_to_response('www/about.html', {}, RequestContext(request))

def adjutor(request):
    # adjutor/
    return render_to_response('www/adjutor.html', {}, RequestContext(request))

def portfolio(request):
    # portfolio/
    return render_to_response('www/portfolio.html', {}, RequestContext(request))

def contact(request):
    # contact/
    if request.method == "POST":
        try:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = 'DallinLauritzen.com: %s' % (request.POST.get('subject', ''))
            message = 'From: %s <%s>\n\n%s' % (name, email, request.POST.get('message', ''))
            to_addrs = ['dallin@dallinlauritzen.com']
            send_mail(subject, message, settings.EMAIL_HOST_USER, to_addrs, fail_silently=False)
            messages.success(request, 'Your message was sent!')
            return redirect(reverse('www.home'))
        except smtplib.SMTPException as e:
            messages.error(request, 'Error connecting to email server. Please send your message manually.<br />%s' % e)
            return redirect(reverse('www.contact'))
        except BadHeaderError as e:
            messages.error(request, 'Nice try, but the data you provided was invalid.')
            return redirect(reverse('www.contact'))
    else:
        return render_to_response('www/contact.html', {}, RequestContext(request))

