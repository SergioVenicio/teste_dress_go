from django.test import TestCase
from core.models import Usuario, Aluguel, Produto


class CriacaoUsuario(TestCase):
    def setUp(self):
        Usuario.objects.create_user('teste@teste.com', 'teste')

    def test_usuario(self):
        usuario = Usuario.objects.get(email='teste@teste.com')
        self.assertEqual(usuario.email, 'teste@teste.com')


class CriacaoAluguel(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create_user('teste@teste.com', 'teste')
        produto = Produto.objects.create(
            nome='teste', valor=100, quantidade=1, imagen='teste.jpg'
        )
        print(produto)
        Aluguel.objects.create(
            cliente=usuario, produto=produto,
            valor='100', cep='10'
        )

    def test_aluguel(self):
        aluguel = Aluguel.objects.filter(valor='100', cep='10').last()
        self.assertEqual(
            aluguel.valor,
            Aluguel.objects.filter(valor='100', cep='10').last().valor
        )
