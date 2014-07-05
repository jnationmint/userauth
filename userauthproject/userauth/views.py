from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

from django.contrib.auth.models import User

from userauth.models import UserProfile
from userauth.forms import UserForm, UserProfileForm

def index(request):
	context = RequestContext(request)
	
	return render_to_response('index.html', {}, context)

def register(request):
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':						#	Condition 1 
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:												#	Condition 2
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	return render_to_response('register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method=='POST':					#	Condition 1
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Account disabled")
		else:
			return render_to_response('login.html', {'wrongcred': 1}, context)
	else:
		return render_to_response('login.html', {}, context)

	return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')	

@login_required
def showprofile(request):
	context = RequestContext(request)
		
	user = request.user
	name = user.username
	email = user.email

	try:
		website = user.userprofile.website
		opinion = user.userprofile.opinion
		msg = "Everything looks good!"
	except:
		msg = "You haven't configured a profile for this user"
		website = "No website"
		opinion = "No opinion"
		
	


	return render_to_response('profile.html', {'name': name, 'email': email, 'website': website, 'opinion': opinion, "msg": msg}, context)

