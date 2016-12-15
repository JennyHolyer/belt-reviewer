from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import User

def index(request):
	if not 'first_name' in request.session:
		request.session['first_name'] = ""

	return render(request, "belt/index.html")

def success(request):

	first_name = request.session['first_name']

	return render(request, "belt/success.html",)

def register_process(request):
	errors =[]
	if request.method == "POST":
		result = User.userMgr.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])

		if result[0]==True:
			request.session['first_name'] = result[1].first_name
			print result, "*******************************************************"
			# request.session.pop('errors')
			return redirect('/books')
		else:
			request.session['errors'] = result[1]
			return redirect('/')
	else:

		return redirect ('/')

def login_process(request):
	errors =[]
	result = User.userMgr.login(request.POST['email'],request.POST['password'])

	if result[0] == True:
		request.session['first_name'] = result[1][0].first_name
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		return redirect('/books')
	else:
		request.session['errors'] = result[1]
		return redirect('/')

def books(request):
	return render(request, "belt/success.html")

def add_book(request):
	return render(request, "belt/add_book.html")

def add_book_process(request):
	return redirect('books/id')


def add_review(request):
	return render(request, "belt/single_book_review.html")

def add_review_process(request):
	return redirect('books/id')

def delete_review(request):
	return redirect('/')

def dashboard(request):
	return render(request, "belt/dashboard.html")

def logout(request):
	return redirect('/')
