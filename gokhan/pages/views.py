from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from . forms import ContactForm
from django.urls import reverse_lazy
from .models import Test, Category



class IndexView(TemplateView):
    template_name = 'index.html'
    tests = Test.objects.all()
    categories = Category.objects.all()
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tests'] = Test.objects.all()
            context['categories'] = Category.objects.all()

        
            return context

class TestView(TemplateView):
    template_name = 'tests.html'
    tests = Test.objects.all()
    categories = Category.objects.all()
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tests'] = Test.objects.all()
            context['categories'] = Category.objects.all()

        
            return context


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Mesajınızı Aldık'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'about.html'

def category_list(request, category_slug):
    tests = Test.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()


    context = {
        'tests': tests,
        'categories': categories,
        'category':Category
    }

    return render(request, 'tests.html', context)