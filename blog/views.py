from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Autor, Articulo
from forms import ArticuloForm
# Create your views here.


def home(request):
	return HttpResponse("HOLA MUNDO!")

def posts(request):
	articulos = Articulo.objects.all()

	return HttpResponse(articulos)

def lista(request):
	posts = Articulo.objects.all()
	form = ArticuloForm()
	context = {'posts':posts, 'form':form}
	return render(request, 'lista.html', context)
	

def post(request, post_id):
	post = Articulo.objects.get(id=post_id)
	context = {'post':post}
	return render(request, 'post.html', context)
	#return HttpResponse(post.texto)	

def add(request):
	if request.method == 'POST':
		form = ArticuloForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ArticuloForm()

	context = {'form':form}
	return render(request, 'add.html', context)
