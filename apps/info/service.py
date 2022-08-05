from apps.info.models import ActiveAll
from django_filters import rest_framework as filters

# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass

class ActiveFilter(filters.FilterSet):
    int = filters.RangeFilter()
    date = filters.DateFilter()
    # date = filters.
    class Meta:
        model = ActiveAll
        fields = ['date', 'int']