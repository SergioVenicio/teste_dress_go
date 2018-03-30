# Teste de cógido dress and go

Para rodar o projeto é necessario criar uma virtualenv com python3.5 e instalar os pacotes listados em requirements.txt com o comando pip install -r requirements.txt, criar o banco de dados com o comando ./manager makemigrate e ./manager migrate e criar um usuário com o comando ./manager createuser.
A url para o cadastro de produtos é /admin/core/produto/add/, a url da imagem dos produtos está em /static/img/.
A url raiz da api é /api/v1/, contanto com a url /api/v1/produtos que lista todos os produtos cadastrados no banco de dados com o metodo GET.
