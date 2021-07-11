from django import forms
from django.forms.formsets import formset_factory


class SalesSearchForm(forms.Form):
    CHART_CHOICES = (
        ("1", "Bar Chart"),
        ("2", "Pi Chart"),
        ("3", "Line Chart"),
    )
    date_from = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
