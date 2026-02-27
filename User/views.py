from django.shortcuts import render , redirect
from .models import *
from django.core.mail import send_mail



def index(request):
    if 'email' in request.session:
        sitters = Sitters_category.objects.all()
        return render(request, "index.html",{'session':True,'sitters':sitters})
    else:
        sitters = Sitters_category.objects.all()
        return render(request, "index.html",{'sitters':sitters})


def register(request):
    if request.method == 'POST':
        a = Customer()
        a.name = request.POST['uname']
        a.email = request.POST['email']
        a.mobile = request.POST['mob']
        a.address = request.POST['add']
        a.password = request.POST['password']
        b = Customer.objects.filter(email = request.POST['email'])
        error_msg = None
        if a.email:
            if len(a.mobile) == 10:
                if len(b) > 0:
                    return render(request,'register.html',{'email':'This email is already registered..'})
                else:
                    if request.POST['password'] == request.POST['cp']:
                        a.save()
                        return redirect('logreg')
                    else:
                        return render(request,'register.html',{'pass':'Passwords did not matched...'})
            else:
                error_msg = "Phone number must be 10 didgits.."
                return render(request,'register.html',{'error':error_msg})
        else:
            error_msg = "Email field is required.."
            return render(request,'register.html',{'error':error_msg})
    else:
        return render(request,'register.html',{})

def logreg(request):
    if request.method == 'POST':
        try:
            a = Customer.objects.get(email = request.POST['email'])
            if a.password == request.POST['password']:
                request.session['email'] = a.email
                request.session['userid'] = a.pk
                return redirect('index')
            else:
                return render(request,'login.html',{'invalid':'Invalid credentials!!!'})
        except:
            return render(request,'login.html',{'reg':'Please register first!!!'})
    else:
        return render(request,'login.html',{'foruser':'userreg'})

def logout(request):
    del request.session['email']
    return redirect('index')


def contact(request):
    if request.method == 'POST':
        store = Contact()
        store.name = request.POST['name']
        store.email = request.POST['email']
        store.mobile = request.POST['mob']
        store.message = request.POST['message']
        store.save()    
        email = str(store.email)
        send_mail(
            'From Baby sitters',
            'Thank you for contacting us , we will answer to you query soon..',
            'pqr6997@gmail.com',
            [email],
            fail_silently = False           
        )
        if 'email' in request.session:
            return render(request, "contact.html",{'session':True,'email':"Email has been sent , will update you shortly."})
        else:
            return render(request, "contact.html",{'email':"Email has been sent , will update you shortly."})
    else:
        return render(request, "contact.html",{})


def services(request):
    return render(request, "services.html")


def details(request):
    return render(request, "details.html")


def sitters(request):
    return render(request, "sitters.html")


def book(request):
    return render(request, "book.html")
