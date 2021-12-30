from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime


# Create your views here.
def home(request):
    ndata = notification.objects.all().order_by('-id')[0:4]
    edata = events.objects.all().order_by('-id')[0:4]
    sdata=slider.objects.all().order_by('-id')
    return render(request, 'user/index.html', {'d': ndata, 'event': edata,'slider':sdata})


def about(req):
    return render(req, 'user/about.html')


def contactus(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        Mobile = request.POST.get("mobile", "")
        Message = request.POST.get("msg", "")
        contact(name=Name, email=Email, mobile=Mobile, message=Message).save()
        status = True
    return render(request, 'user/contactus.html', {'S': status})


def login(req):
    return render(req, 'user/login.html')


def memberships(req):
    cdata = city.objects.all().order_by('cityname')
    if req.method == "POST":
        name = req.POST.get("name", "")
        dob = req.POST.get("dob", "")
        gender = req.POST.get("gen", "")
        email = req.POST.get("email", "")
        mob = req.POST.get("mobile", "")
        profession = req.POST.get("prof", "")
        cityname = req.POST.get("cityname", "")
        picture = req.FILES['fu']
        address = req.POST.get("address", "")
        a = membership.objects.filter(email=email)
        if a.count() > 0:
            return HttpResponse(
                "<script>alert('You are already registered...');window.location.href='/user/membership/'</script>")
        else:
            membership(name=name, dob=dob, email=email, mobile=mob, profession=profession, cityname=cityname,
                       gender=gender, address=address, picture=picture, mdate=datetime.datetime.now()).save()
            return HttpResponse(
                "<script>alert('You are registered successfully...');window.location.href='/user/membership/'</script>")
    return render(req, 'user/membership.html', {"city": cdata})


def donates(req):
    ddata = city.objects.all().order_by('cityname')
    if req.method == "POST":
        name = req.POST.get("name", "")
        email = req.POST.get("email", "")
        mob = req.POST.get("mobile", "")
        occupation = req.POST.get("occupation", "")
        cityname = req.POST.get("cityname", "")
        address = req.POST.get("address", "")
        amount = req.POST.get("amount", "")
        donate(name=name, email=email, mobile=mob, occupation=occupation, cityname=cityname, address=address,
               amount=amount, ddate=datetime.datetime.now()).save()
        return HttpResponse(
            "<script>alert('Thanks for donating, Your donation can help someone...');window.location.href='/user/donate/'</script>")
    return render(req, 'user/donateNow.html', {"city": ddata})


def event(req):
    edata = events.objects.all().order_by('-id')
    return render(req, 'user/ourEvent.html', {"event": edata})


def imagegallery(request):
    gdata = gallery.objects.all()
    mydict = {"d": gdata}
    return render(request, 'user/gallery.html', mydict)

def videogallery(request):
    vdata=video.objects.all()
    return render(request,'user/VideoGallery.html',{"video":vdata})

def privacy(request):
    return render(request,'user/Privacy Policy.html')

def Terms(request):
    return render(request,'user/termCondition.html')