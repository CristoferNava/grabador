from django.views.generic import TemplateView
from django.shortcuts import render
from form.forms import ContactForm

class Form(TemplateView):
    template_name = 'form/form.html'

    def get(self, request):
        form = ContactForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
            args = {
                'form': form,
            }

            return render(request, self.template_name, args)