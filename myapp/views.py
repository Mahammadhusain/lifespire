from django.shortcuts import render
from .form import ContactForm
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Email sending function
def email_me(data):
    dynamic_data = {
        'inquiry_data': 'Dynamic Content',
    }
    html_message = render_to_string("email_template.html",dynamic_data)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject = "Distributor & Retailer Inquiry", 
        body = plain_message,
        from_email = "kadiwala.530@gmail.com" ,
        to = ["kadiwala.530@gmail.com"])

    message.attach_alternative(html_message, "text/html")
    message.send()


# Create your views here.
def HomeView(request):
    context = {"h": "Hello world with django"}
    return render(request, "home.html", context)


def DistributorRetailer(request):
    form = ContactForm(label_suffix='')
    if request.method == "POST":
        form = ContactForm(label_suffix='')
        if form.is_valid():
            form.save()
            email_me(form.cleaned_data)
            return render(request, "distributor_retailer.html", {"form": form, "success": True})
        else:
            print(form.errors)
            return render(request, "distributor_retailer.html", {"form": form, "success": False})
    context = {"form": form}
    return render(request, "distributor_retailer.html", context)


def AllproductsView(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "allproducts.html", context)


def SingleproductsView(request):
    context = {"h": "Hello world with django"}
    return render(request, "singleproduct.html", context)


def AllblogsView(request):
    context = {"h": "Hello world with django"}
    return render(request, "allblogs.html", context)


def SingleblogView(request):
    context = {"h": "Hello world with django"}
    return render(request, "singleblog.html", context)


def AboutusView(request):
    context = {"h": "Hello world with django"}
    return render(request, "aboutus.html", context)


def ContactusView(request):
    context = {}
    return render(request, "contactus.html", context)
