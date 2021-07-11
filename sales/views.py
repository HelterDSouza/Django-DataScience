from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Sale


def home_view(request):
    return render(request, "sales/home.html", {})


class SaleListView(ListView):
    """
    def sale_list_view(request):
        sales = Sale.object.all()
        return render(request, 'sales/main.html', {'sales':sales})

    """

    model = Sale
    template_name = "sales/main.html"
    context_object_name = "sales"


class SaleDetailView(DetailView):
    """
    def sale_detail_view(request,pk):
        sale = Sale.object.get(pk=pk)
        or
        sale = get_object_or_404(Sale,pk=pk)
        return render(request,'sales/detail.html',{'sale':sale})

    """

    model = Sale
    template_name = "sales/detail.html"
