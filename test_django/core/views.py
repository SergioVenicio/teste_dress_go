from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from core.models import Produto, Usuario, Aluguel
from core.forms import UsuarioForm, UsuarioAddForm, AluguelForm
from django.http import HttpResponseForbidden
from django.contrib.auth import login as login_user
from core.serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


def home(request):
    produtos = Produto.objects.filter(quantidade__gt=0)
    context = {
        'produtos': produtos
    }
    return render(request, 'core/home.html', context)


def produto(request, id):
    produto = Produto.objects.get(pk=id)
    if request.method == "POST":
        cep = request.POST.get('cep', None)
        quantidade = request.POST.get('quantidade', None)
        if quantidade is not None and int(quantidade) > 0:
            if produto.quantidade < int(quantidade):
                context = {
                    'quantidade_error': True,
                    'produto': produto
                }
            else:
                produto.quantidade -= int(quantidade)
                valor = int(quantidade) * produto.valor
                try:
                    usuario = Usuario.objects.get(pk=request.user.id)
                    aluguel = Aluguel(
                        cliente=usuario, produto=produto, valor=valor, cep=cep
                    )
                    produto.save()
                    aluguel.save()
                    context = {
                        'aluguel': True,
                        'produto': produto
                    }
                except Usuario.DoesNotExist:
                    context = {
                        'produto': produto,
                        'login_required': True
                    }
        else:
            context = {
                'quantidade_zero': True,
                'produto': produto
            }
        return render(request, 'core/produto.html', context)
    else:
        context = {
            'produto': produto
        }
        return render(request, 'core/produto.html', context)


def user_add(request):
    form = UsuarioAddForm()

    if request.method == 'POST':
        form = UsuarioAddForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            password_confirm = request.POST.get('password_confirm', None)

            if password != password_confirm:
                context = {
                    'form': form,
                    'password_error': True
                }
                return render(request, 'core/user_add.html', context)
            else:
                usuario = Usuario.objects.create_user(email, password)
                login_user(request, usuario)
                return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'core/user_add.html', context)
    else:
        context = {
            'form': form
        }
        return render(request, 'core/user_add.html', context)


def alugueis(request):
    if request.user.is_admin:
        alugueis = Aluguel.objects.all()
        context = {
            'alugueis': alugueis
        }
        return render(request, 'core/alugueis.html', context)
    else:
        raise HttpResponseForbidden()


def edit_aluguel(request, id):
    aluguel = Aluguel.objects.get(pk=id)

    if request.method == 'POST':
        form = AluguelForm(request.POST, instance=aluguel)
        if form.is_valid():
            aluguel = form.save()
    else:
        form = AluguelForm(
            instance=aluguel
        )

    context = {
        'aluguel': aluguel,
        'form': form
    }
    return render(request, 'core/edit_aluguel.html', context)


def login(request):
    form = UsuarioForm()
    context = {
        'form': form
    }
    return render(request, 'core/login.html', context)
