from django.db import models


# Create your models here.
class Customer(models.Model):
    """Classe dos clientes no banco de dados"""

    # Campo nome de cada cliente
    name = models.CharField(max_length=120)
    # imagem de cada cliente upload_to=pasta customers contendo as imagens, default=se o cliente nao colocar imagem, sera usado uma imagem padrão
    logo = models.ImageField(upload_to="customers", default="no_picture.png")

    def __str__(self) -> str:
        return str(self.name)
