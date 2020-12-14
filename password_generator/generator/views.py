from django.shortcuts import render
from django.http import HttpResponse

import random

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):
	gen_password = ''

	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend([x.upper() for x in characters])
	if request.GET.get('special'):
		characters.extend(list('!?@#$%^&*()'))
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	length = int(request.GET.get('length', 12))

	for i in range(length):
		gen_password += random.choice(characters)
	return render(request, 'generator/password.html', {'password': gen_password})