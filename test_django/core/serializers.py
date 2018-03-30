from rest_framework import serializers
from core.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return obj.imagen.url

    class Meta:
        model = Produto
        fields = ('__all__')
