from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Destination, Trending, Testimonial
from django.views.generic.detail import DetailView
from django.views import generic
from .forms import ContactForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created succesfully ...")
                return redirect('/login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    dest = Destination.objects.all()
    return render(request, 'destinations.html' , {'dest': dest})
    
def index(request):

    dests = Destination.objects.all()
    trending = Trending.objects.all()
    testimonials = Testimonial.objects.all()


    return render(request, 'index.html', {'dests': dests, "trending":trending, 'testimonials':testimonials})

class DestinationDetailView(DetailView):

    model = Destination
    context_object_name = "destinations"
    template_name = "detail.html"

class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


