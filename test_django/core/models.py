from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('O email é obrigatório')

        usuario = self.model(
            email=self.normalize_email(email)
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('O email é obrigatório')

        usuario = self.create_user(
            email,
            password=password
        )

        usuario.is_admin = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='static/img/')

    def realizar_venda(self, quantidade):
        if int(quantidade > 0):
            if self.quantidade < quantidade:
                return False
            else:
                self.quantidade -= 1
                return True
        else:
            return False

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.cliente, self.produto, self.valor, self.cep
        )
