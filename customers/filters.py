from django_filters import FilterSet, CharFilter, DateFilter

from customers.models import Order


class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gt')
    end_date = DateFilter(field_name='date_created', lookup_expr='lt')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer', 'date_created')