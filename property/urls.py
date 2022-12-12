from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('listing.html',views.listing,name='listing'),
    path('listland.html',views.listland,name='listland'),
    path('myproperty.html',views.propertysingle,name='propertysingle'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('login.html',views.login,name='login.html'),
    path('<id>/myproperty',views.myproperty,name='myproperty'),
    path('addproperty.html',views.addproperty,name='addproperty'),
    path('addproperty',views.addproperty,name="addproperty"),
    path('myproperty',views.myproperty,name='myproperty'),
    path('<id>/update',views.editproperty,name='editproperty'),
    path('addland.html',views.addland,name='addland'),
    path('addland',views.addland,name="addland"),
    path('myland',views.myland,name='myland'),
    path('<id>/myland',views.myland,name='myland'),
    path('<id>/updateland',views.editland,name='editland'),
    path('<id>/delete',views.deleteproperty,name='deleteproperty'),
    path('buyer.html',views.buyer,name='buyer'),
    path('buyer',views.buyer,name="buyer"),
    path('<id>/updateprofile',views.editbuyer,name='editbuyer'),
    path('mybuyer',views.mybuyer,name='mybuyer'),
    path('<id>/mybuyer',views.mybuyer,name='mybuyer'),
    path('',views.topproperties,name='topproperties'),
    path('<id>/detailedproperty',views.detailedproperty,name='detailedproperty'),
    path('detailedproperty',views.detailedproperty,name='detailedproperty'),
    path('toplands.html',views.toplands,name='toplands'),
    path('<id>/detailedland',views.detailedland,name='detailedland'),
    path('detailedland',views.detailedland,name='detailedland'),
    path('<id>/deleteland',views.deleteland,name='deleteland'),
    path('<id>/deleteprofile',views.deleteprofile,name='deleteprofile'),
    path('search',views.search,name='search')
]