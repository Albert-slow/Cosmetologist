from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import CategoryModel, ProcedureModel, CartModel, PostModel, CommentsModel
from .forms import SearchForm


class HomePage(ListView):
    form_class = SearchForm
    template_name = 'index.html'
    model = ProcedureModel
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["procedures"] = ProcedureModel.objects.all()
        context["posts"] = PostModel.objects.all()
        return context


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    if request.method == 'POST':
        get_procedure = request.POST.get('search_procedure')
        try:
            exact_procedure = procedure.objects.get(procedure_title__icontains=get_procedure)
            return redirect(f'/procedure/{exact_procedure.id}')
        except:
            return redirect('/')


def procedure_page(request, pk):
    procedure = ProcedureModel.objects.get(id=pk)
    context = {'procedure': procedure}
    return render(request, 'procedure.html', context)


def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_procedure = ProcedureModel.objects.filter(procedure_category=category)
    context = {'procedure': current_procedure}
    return render(request, 'category.html', context)


def posts_page(request, pk):
    posts = PostModel.objects.get(id=pk)
    context = {'posts': posts}
    return render(request, 'post.html', context)


def post_list(request):
    posts = PostModel.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def contact_us(request):
    template_name = 'contact.html'
    return render(request, template_name='contact.html')

