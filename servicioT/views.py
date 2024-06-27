from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from JR_SISTEMAS import settings
from django.contrib import messages

def servicioT(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        asunto = request.POST['asunto']
        message = request.POST['message']

        template= render_to_string('serviciotecnico/emailtemplate.html', {
           'name': name,
           'email': email,
           'asunto': asunto,
           'message':message,
       })
    
        emailSender = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['jrsistemas57@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()
    
        messages.success (request, 'El correo fue envíado correctamente')

    return render(request, 'serviciotecnico/servicioT.html')