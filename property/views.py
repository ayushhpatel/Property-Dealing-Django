from email import message
from urllib import request
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Property,Land,Buyer
from .forms import PropertyForm,LandForm,BuyerForm
# Create your views here.

def index(request):
    lists=Property.objects.filter(price__range=("10000000","400000000"))
    return render(request,'index.html',{'lists':lists})

def listing(request):
    lists=Property.objects.all()
    return render(request,'listing.html',{'lists':lists})

def topproperties(request):
    lists=Property.objects.filter(price__range=("10000000","400000000"))
    return render(request,'index.html',{'lists':lists})

def toplands(request):
    lands=Land.objects.filter(price__range=("10000000","600000000"))
    return render(request,'index.html',{'lands':lands})

def listland(request):
    lists=Land.objects.all()
    return render(request,'listland.html',{'lists':lists})

def propertysingle(request):
    return render(request,'property-single.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def addproperty(request):
    if(request.method=="POST"):
        seller=request.POST['seller']
        title=request.POST['title']
        house_no=request.POST['hno']
        society=request.POST['society']
        locality=request.POST['locality']
        city=request.POST['city']
        bedrooms=request.POST['beds']
        bathrooms=request.POST['baths']
        area=request.POST['area']
        price=request.POST['price']
        img=request.POST['img']
        desc=request.POST['desc']
        age=request.POST['age']
        contactno=request.POST['contact']
        if(User.objects.filter(username=seller).exists()):
            seller=User.objects.get(username=seller)
            prop=Property(seller=seller,contactno=contactno,title=title,house_no=house_no,society=society,locality=locality,city=city,bedrooms=bedrooms,bathrooms=bathrooms,area=area,price=price,img=img,desc=desc,age=age)
            prop.save()
            messages.info(request,"Property Successfully Added")
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/')
    else:
        return render(request,'addproperty.html')

def myproperty(request,id):
    if(Property.objects.filter(seller_id=id).count()):
        context ={}
        context["data"]= Property.objects.get(seller_id=id)
        return render(request, "myproperty.html", context)
    else:
        messages.info(request,'Invalid access')
        return redirect('/')

def editproperty(request,id):
    if(Property.objects.filter(seller_id=id).count()):
        context ={}
        obj = get_object_or_404(Property, seller_id = id)
        form = PropertyForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+id+"/myproperty")
        context["form"] = form
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "edit.html", context)

def deleteproperty(request,id):
    if(Property.objects.filter(seller_id=id).count()):
        context ={}
        obj=get_object_or_404(Property,seller_id=id)
        if request.method=="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "deleteproperty.html", context)

def addland(request):
    if(request.method=="POST"):
        landseller=request.POST['landseller']
        type=request.POST['type']
        locality=request.POST['locality']
        city=request.POST['city']
        area=request.POST['area']
        price=request.POST['price']
        contactno=request.POST['contact']
        img=request.POST['img']
        if(User.objects.filter(username=landseller).exists()):
            landseller=User.objects.get(username=landseller)
            land=Land(landseller=landseller,contactno=contactno,img=img,type=type,locality=locality,city=city,area=area,price=price)
            land.save()
            messages.info(request,"Land Successfully Added")
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/')
    else:
        return render(request,'addland.html')

def myland(request,id):
    if(Land.objects.filter(landseller_id=id).count()):
        context ={}
        context["data"]=Land.objects.get(landseller_id=id)
        return render(request, "myland.html", context)
    else:
        messages.info(request,'Invalid access')
        return redirect('/')

def editland(request,id):
    if(Land.objects.filter(landseller_id=id).count()):
        context ={}
        obj = get_object_or_404(Land,landseller_id=id)
        form = LandForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+id+"/myland")   
        context["form"] = form
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "edit.html", context)

def buyer(request):
    if(request.method=="POST"):
        buyer=request.POST['buyer']
        incomecertificate=request.POST['incomecert']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        photo=request.POST['photo']
        card=request.POST['card']
        if(User.objects.filter(username=buyer).exists()):
            buyer=User.objects.get(username=buyer)
            buy=Buyer(buyer=buyer,incomecertificate=incomecertificate,phoneno=phoneno,email=email,photo=photo,card=card)
            buy.save()
            messages.info(request,"Buyer details Added")
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/')
    else:
        return render(request,'buyer.html')

def mybuyer(request,id):
    if(Buyer.objects.filter(buyer_id=id).count()):
        context ={}
        context["data"]=Buyer.objects.get(buyer_id=id)
        return render(request, "mybuyer.html", context)
    else:
        messages.info(request,'Invalid access')
        return redirect('/')

def editbuyer(request,id):
    if(Buyer.objects.filter(buyer_id=id).count()):
        context ={}
        if(Buyer.objects.filter(buyer_id=id).count()):
            obj = get_object_or_404(Buyer,buyer_id=id)
            form = BuyerForm(request.POST or None, instance = obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/"+id+"/mybuyer")
            context["form"] = form
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "edit.html", context)

def detailedproperty(request,id):
    if(Property.objects.filter(id=id).values('id').count()):
        context ={}
        context["data"]= Property.objects.get(id=id)
        return render(request, "detailedproperty.html", context)
    else:
        messages.info(request,'Invalid access')
        return redirect('/')

def detailedland(request,id):
    if(Land.objects.filter(id=id).count()):
        context ={}
        context["data"]= Land.objects.get(id=id)
        return render(request, "detailedland.html", context)
    else:
        messages.info(request,'Invalid access')
        return redirect('/')

def deleteland(request,id):
    if(Land.objects.filter(landseller_id=id).count()):
        context ={}
        obj=get_object_or_404(Land,landseller_id=id)
        if request.method=="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "deleteland.html", context)

def deleteprofile(request,id):
    if(Buyer.objects.filter(buyer_id=id).count()):
        context ={}
        obj=get_object_or_404(Buyer,buyer_id=id)
        if request.method=="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        messages.info(request,'Invalid access')
        return redirect('/')
    return render(request, "deleteprofile.html", context)

def search(request):
    if(request.method=="POST"):
        type=request.POST['ext']
        city=request.POST['city']
        if(type=="Property"):
            if(Property.objects.filter(city=city).values('city').count()):
                sproperties=Property.objects.filter(city=city)
                return render(request, "searchproperty.html", {'properties':sproperties})
            else:
                messages.info(request,'No property available in this city')
                return redirect('/')
        elif(type=="Land"):
            if(Land.objects.filter(city=city).values('city').count()):
                lands=Land.objects.filter(city=city)
                return render(request, "searchland.html", {'lands':lands})
            else:
                messages.info(request,'No Land available in this city')
                return redirect('/')
    else:
        return redirect('')