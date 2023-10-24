from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', HomeView,name='home'),
    path('distributorretailer/', DistributorRetailer,name='distributorretailer'),
    path('allproducts/', AllproductsView,name='allproducts'),
    path('singleproduct/', SingleproductsView,name='singleproduct'),
    path('allblogs/', AllblogsView,name='allblogs'),
    path('singleblog/', SingleblogView,name='singleblog'),
    path('aboutus/', AboutusView,name='aboutus'),
    path('contactus/', ContactusView,name='contactus'),
 
]
