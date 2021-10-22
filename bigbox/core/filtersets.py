""" Filters of model core. """

from django_filters import rest_framework as filters

from . import models


class ActivityFilter(filters.FilterSet):
    category_id = filters.NumberFilter(field_name='category_id')
    reasons = filters.NumberFilter(field_name='reasons')
    slug = filters.CharFilter(field_name='slug', lookup_expr='icontains')

    class Meta:
        model = models.Activity
        fields = ["category", "slug", "reasons__id"]
