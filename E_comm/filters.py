import django_filters
from .models import Item


# Here GTE = greater than equal to and LTE = Less than equal to
class ItemFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name="created_at", lookup_expr="gte", label="From Date")
    to_date = django_filters.DateFilter(field_name="created_at", lookup_expr="lte", label="To Date")
    search = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Search")

    class Meta:
        model = Item
        fields = ["from_date", "to_date", "search"]