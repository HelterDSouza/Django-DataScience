from django.contrib import admin

from .models import Customer

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Classe para acessar os cliente no painel de administração

    Arguments:
        admin {[type]} -- [description]
    """

    pass
