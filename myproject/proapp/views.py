from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from proapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def index(request):
    return render(request,'apps/index.html')
def shop(request):
    return render(request,'apps/shop.html')
def men(request):
    return render(request,'apps/men.html')
def women(request):
    return render(request,'apps/women.html')
def Beauty(request):
    return render(request,'apps/beauty.html')
def footwear(request):
    return render(request,'apps/footwear.html')
def zworld(request):
    return render(request,'apps/z-world.html')
def kids(request):
    return render(request,'apps/kids.html')
def contact(request):
    return render(request,'apps/contact.html')
@login_required
def login(request):
	return render(request,'registration/login.html')
def logout(request):
    return render(request,'apps/logout.html')
def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'apps/signup.html',{'form':form})



