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
	''' Obtiene todos los articulos los envia al template lista.html '''
	posts = Articulo.objects.all() # SELECT * FROM Articulo;
	context = {'posts':posts}
	return render(request, 'lista.html', context)
	

def post(request, post_id):
	''' 
	Obtiene un post especifico, la id la obtiene 
	de la url y lo envia a template post.html
	'''
	post = Articulo.objects.get(id=post_id) # SELECT * FROM Articulo WHERE id=$post_id;
	context = {'post':post}
	return render(request, 'post.html', context)
	#return HttpResponse(post.texto)	

def add(request):
	'''
	Si el metodo HTTP no es POST muestra el formulario, si es post valida
	el formulario e impacta en la base de datos.
	Envia todo al template add.html
	'''
	if request.method == 'POST':
		form = ArticuloForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ArticuloForm()

	context = {'form':form}
	return render(request, 'add.html', context)
