import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .form import SalesSearchForm

# Create your views here.
from .models import Sale
from .utils import get_customer_from_id, get_salesman_from_id


def home_view(request):
    sales_df = None
    merged_df = None
    positions_df = None
    form = SalesSearchForm(request.POST or None)
    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        sales_qs = Sale.objects.filter(
            created__date__lte=date_to, created__date__gte=date_from
        )
        if len(sales_qs) > 0:
            sales_df = pd.DataFrame(sales_qs.values())
            sales_df["customer_id"] = sales_df["customer_id"].apply(
                get_customer_from_id
            )
            sales_df["salesman_id"] = sales_df["salesman_id"].apply(
                get_salesman_from_id
            )
            sales_df["created"] = sales_df["created"].apply(
                lambda x: x.strftime("%Y-%m-%d")
            )
            sales_df.rename(
                {
                    "customer_id": "customer",
                    "salesman_id": "salesman",
                    "id": "sales_id",
                },
                axis=1,
                inplace=True,
            )
            positions_data = []
            for sale in sales_qs:
                for pos in sale.get_positions():
                    obj = {
                        "position_id": pos.id,
                        "product": pos.product.name,
                        "quantity": pos.quantity,
                        "price": pos.price,
                        "sales_id": pos.get_sales_id(),
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(sales_df, positions_df, on="sales_id")

            # Convert to HTML
            positions_df = positions_df.to_html(classes="table").replace(
                "<thead>", "<thead class='thead-light'>"
            )
            sales_df = sales_df.to_html(classes="table").replace(
                "<thead>", "<thead class='thead-light'>"
            )
            merged_df = merged_df.to_html(classes="table").replace(
                "<thead>", "<thead class='thead-light'>"
            )
        else:
            pass
    context = {
        "form": form,
        "sales_df": sales_df,
        "positions_df": positions_df,
        "merged_df": merged_df,
    }
    return render(request, "sales/home.html", context)


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
