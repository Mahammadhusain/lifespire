from django.shortcuts import render

# Create your views here.
def HomeView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'home.html',context)
def AllproductsView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'allproducts.html',context)
def SingleproductsView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'singleproduct.html',context)
def AllblogsView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'allblogs.html',context)
def SingleblogView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'singleblog.html',context)
def AboutusView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'aboutus.html',context)
def ContactusView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'contactus.html',context)
