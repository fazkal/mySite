from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.forms import contactForm,newsletterForm
from django.contrib import messages

def index_view(requests):
    return render (requests,'website/index.html')

def about_view(requests):
    return render (requests,'website/about.html')

def contact_view(requests):
    if requests.method=='POST':
        form=contactForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.add_message(requests,messages.SUCCESS,'Your message has been submited.')
        else:
            messages.add_message(requests,messages.ERROR,'Your message failed.')
    form=contactForm()
    return render (requests,'website/contact.html',{'form':form})

def newsletter_view(requests):
    if requests.method=='POST':
        form=newsletterForm(requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
       return HttpResponseRedirect('/')


