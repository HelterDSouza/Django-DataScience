from django.db import models


# Create your models here.
class Product(models.Model):
    # nome do Produto
    name = models.CharField(max_length=120)
    # imagem do produto
    image = models.ImageField(upload_to="products", default="no_picture.png")
    # preço
    price = models.FloatField(help_text="Em real R$")
    # auto_now_add salva o atual timestamp quanto o objeto é criado no banco de dados
    created = models.DateTimeField(auto_now_add=True)
    # auto_now atualiza o atual timestamp toda vez que o objeto e salvo (last modified)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.created.strftime('%d/%m/%Y')}"
