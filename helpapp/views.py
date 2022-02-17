from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.
from helpapp.models import Contact, Predonation


def header(request):
    return render(request, 'html/header.html')

def header1(request):
    return render(request, 'html/header1.html')

def home(request):
    return render(request, 'html/home.html')
def home1(request):
    return render(request, 'html/home1.html')


def footer(request):
    return render(request, 'html/footer.html')


def about(request):
    return render(request, 'html/about.html')

def about1(request):
    return render(request, 'html/about1.html')


def media(request):
    return render(request, 'html/media.html')
def blog1(request):
    return render(request, 'html/blog1.html')


def creg(request):
    return render(request, 'html/curegistration.html')


def login(request):
    return render(request, 'html/customerlogin.html')


def spologin(request):
    return render(request, 'html/sponsorlogin.html')


def predonation(request):
    return render(request, 'html/predonation.html')


def sreg(request):
    return render(request, 'html/spregistration.html')



def report(request):
    return render(request, 'html/reports.html')
def report1(request):
    return render(request, 'html/report1.html')

def login1save(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'html/home.html')
        else:
            messages.info(request, 'Invalid Password or Username.Try again')
            return render(request, 'html/customerlogin.html')
    else:
        return render(request, 'html/customerlogin.html')


def register1(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, 'html/curegistration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return render(request, 'html/curegistration.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                c = "User created Sucessfully"
                return render(request, 'html/curegistration.html', {'c': c})
        else:
            m = "Password not matched"
            return render(request, 'html/curegistration.html', {'m': m})

        return render(request, 'html/curegistration.html')
    else:
        return render(request, 'html/curegistration.html')


def logout1(request):
    auth.logout(request)
    return render(request, 'html/home.html')
def logout1new(request):
    auth.logout(request)
    return render(request, 'html/home1.html')


def login2save(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'html/home1.html')
        else:
            messages.info(request, 'Invalid Password or Username.Try again')
            return render(request, 'html/sponsorlogin.html')
    else:
        return render(request, 'html/sponsorlogin.html')


def register2(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, 'html/spregistration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return render(request, 'html/spregistration.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                c = "User created Sucessfully"
                return render(request, 'html/spregistration.html', {'c': c})
        else:
            m = "Password not matched"
            return render(request, 'html/spregistration.html', {'m': m})
        return render(request, 'html/spregistration.html')
    else:
        return render(request, 'html/spregistration.html')


def logout2(request):
    auth.logout(request)
    return render(request, 'html/home.html')

def logout2new(request):
    auth.logout(request)
    return render(request, 'html/home1.html')


def contactsave(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        message = request.POST.get("message")
        try:
            a=Contact(name=name, phone=phone, city=city, message=message)
            a.save()
            m = "Send Successfully, Thank You for Contact Us. You will get a Email Notification."
            return render(request, 'html/home.html', {'m': m})
        except:
            return render(request, 'html/home.html')
    else:
        return render(request, 'html/home.html')


def show(request):
    member = Contact.objects.all()
    return render(request, 'html/showreport1.html', {'member': member})

def show2new(request):
    member = Contact.objects.all()
    return render(request, 'showreport2.html', {'member': member})



def delete(request, id):
    m = Contact.objects.get(id=id)
    m.delete()
    return redirect('/helpapp/show')

def deletenew(request, id):
    m = Contact.objects.get(id=id)
    m.delete()
    return redirect('/helpapp/show2new')


def save1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        check = request.POST.get("check")
        bank = request.POST.get("bank")
        accno = request.POST.get("accno")
        try:
            a = Predonation(name=name, address=address, city=city, phone=phone, email=email, amount=amount, check=check,bank=bank,accno=accno)
            a.save()
            b = "Payment done. Thank you For Your Contribution"
            return render(request, 'html/predonation.html', {'b': b})
        except:
            return render(request, 'html/predonation.html')
    else:
        return render(request, 'html/predonation.html')


def show1(request):
    member1 = Predonation.objects.all()
    return render(request, 'html/show2.html', {'member1': member1})

def shownew(request):
    member1 = Predonation.objects.all()
    return render(request, 'html/show2new.html', {'member1': member1})



def delete1(request, Pre_id):
    n = Predonation.objects.get(Pre_id=Pre_id)
    n.delete()
    return redirect('/helpapp/show1')


def delete1new(request, Pre_id):
    n = Predonation.objects.get(Pre_id=Pre_id)
    n.delete()
    return redirect('/helpapp/show2new')

