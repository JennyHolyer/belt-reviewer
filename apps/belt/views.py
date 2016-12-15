from django.shortcuts import render

def index (request):
	return render (request, 'belt/index.html')

# Create your views here.
