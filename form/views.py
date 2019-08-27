from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.shortcuts import render
from form.forms import ContactForm

class Form(TemplateView):
    template_name = 'form/form.html'

    def get(self, request):
        form = ContactForm
        return render(request, self.template_name, {'form': form})

    '''
    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
            args = {
                'form': form,
            }

            return render(request, self.template_name, args)
    '''

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        body = render_to_string(
            'form/email_content.html', {
                'name': name,
                'email': email,
                'text': text,
            },
        )

        email_message = EmailMessage(
            subject = 'Mensaje de usuario',
            body = body,
            from_email=email,
            to=['cj.carmonanava@utgo.mx']
        )
        email_message.content_subtype = 'html'
        email_message.send()
    
