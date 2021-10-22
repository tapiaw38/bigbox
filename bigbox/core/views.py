from rest_framework import pagination, viewsets

from . import models, serializers, filtersets, paginations

from django_filters import rest_framework as filters


class BoxViewSet(viewsets.ModelViewSet):
    """ A ViewSet  of the box model """

    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer
    lookup_field = 'slug'


class ActivityViewSet(viewsets.ModelViewSet):
    """ A ViewSet of the Activity model """
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filtersets.ActivityFilter
    pagination_class = paginations.CustomPagination


# Category viewset
class CategoryViewSet(viewsets.ModelViewSet):
    """ A ViewSet of the Category model """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
