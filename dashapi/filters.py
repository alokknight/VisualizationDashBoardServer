import django_filters
from .models import DataPoint

class DataPointFilter(django_filters.FilterSet):
    end_year   = django_filters.CharFilter(lookup_expr='icontains')
    start_year = django_filters.CharFilter(lookup_expr='icontains')
    country    = django_filters.CharFilter(lookup_expr='icontains')
    topic      = django_filters.CharFilter(lookup_expr='icontains')
    sector     = django_filters.CharFilter(lookup_expr='icontains')
    published  = django_filters.DateFilter(field_name='published', lookup_expr='icontains')
    impact     = django_filters.CharFilter(lookup_expr='icontains')
    relevance  = django_filters.CharFilter(lookup_expr='icontains')
    likelihood = django_filters.CharFilter(lookup_expr='icontains')
    region = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DataPoint
        fields=[]
        # fields = ['end_year','start_year','published','impact','relevance','likelihood']
        # form = False

