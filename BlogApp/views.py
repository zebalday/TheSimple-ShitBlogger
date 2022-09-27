from msilib.schema import ListView
from django.core.paginator import Paginator
from .models import Article, Category, MiscLinks, SocialMedia
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Vista basada en clase de la página de inicio
class Index(TemplateView):
    # Nombre de la plantilla
    template_name = 'Index.html'
    
    # Contexto de la página
    PageContext = {
        'PageTitle':'Inicio',
        'ContentTitle':'INICIO'
    }

    def get(self, request):
        return render(request, self.template_name, self.PageContext)


# Vista basada en clase de la página de inicio de sesión
class Login(TemplateView):
    # Nombre de la plantilla
    template_name = 'Login.html'
    
    # Contexto de la página
    PageContext = {
        'PageTitle': 'Login',
        'ContentTitle':'LOGIN'
    }

    def post(self, request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user != None:
                login(request, user)
                return redirect("Index")
            
            else:
                messages.warning(request, "Nombre o contraseña incorrectos")
                return redirect("Login")

        
        else:
            return render(request, self.template_name, self.PageContext)


# Vista basada en clase para cerrar sesión
class Logout(TemplateView):
    def get (self, request):
        logout(request)
        return redirect("Index")


# Vista basada en clase de la página de ShitPosts 
# (Todos los posts separados por paginador)
class AllShitPosts(TemplateView):
    # Nombre de la plantilla y registros de los posts.
    template_name = 'AllShitPosts.html'
    posts = Article.objects.all().order_by('-created_at')

    # Contexto de la página
    PageContext = {
        'PageTitle': 'Posts',
        'ContentTitle':'SHITPOSTS',
    }

    def get(self, request):
        # Crea paginador de posts y agrega al contexto de la página
        paginator = Paginator(self.posts, 1)
        page = request.GET.get('page')
        page_article = paginator.get_page(page)
        self.PageContext['Posts'] = page_article
        return render(request, self.template_name, self.PageContext)




    
