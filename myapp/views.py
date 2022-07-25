from django.shortcuts import render

# Create your views here.
def HomeView(request):
    context = {
      'h':'Hello world with django'
    }
    return render(request,'index.html',context)
