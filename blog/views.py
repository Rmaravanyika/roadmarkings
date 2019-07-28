from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

from .forms import ContactForm
from .models import BlogPost, Contact


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def contact(request):
    form = ContactForm(request.POST or None)
    success = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = ContactForm()
            success =True
            messages.success(request, 'Your Message has been submitted, our team will be intouch soon.')

    posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:1]
    return render(request, 'contact.html', {'form': form, 'posts':posts})	

def post_detail(request, pk):
	post = get_object_or_404(BlogPost, pk=pk)
	return render(request, 'blog_details.html')

def blogg_page(request):
    posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogg.html', {'posts': posts})


# Create your views here.
