from django.db.models import fields
from rest_framework import serializers

from . import models


# View Activity

class ReasonSerializer(serializers.ModelSerializer):
    """ A Reason Serializer. """

    class Meta:
        model = models.Reason
        fields = (
            "id",
            "name",
            "order",
            "slug"
        )


class ActivityImageSerializer(serializers.ModelSerializer):
    """ A ActivityImage Serializer. """

    class Meta:
        model = models.ActivityImage
        fields = (
            "id",
            "order",
            "upload"
        )


class ActivitySerializer(serializers.ModelSerializer):
    """ A Activity Serializer. """

    reasons = ReasonSerializer(many=True, allow_null=True)
    activityimage_set = ActivityImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Activity
        fields = (
            'name',
            'slug',
            'internal_name',
            'description',
            'category',
            'purchase_available',
            'reasons',
            'activityimage_set',
        )


# View Box

class BoxImageSerializer(serializers.ModelSerializer):
    """ A serializer image box. """

    class Meta:
        model = models.BoxImage
        fields = (
            "id",
            "order",
            "upload"
        )


class BoxSerializer(serializers.ModelSerializer):
    """ A serializer for box. """

    boximage_set = BoxImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Box
        fields = (
            "name",
            "slug",
            "category",
            "description",
            "purchase_available",
            "price",
            "boximage_set"
        )
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}


# View Category

class BoxChildSerializer(serializers.ModelSerializer):
    """ A serializer for box. """

    class Meta:
        model = models.Box
        fields = (
            "name",
            "slug",
            "price"
        )


class CategorySerializer(serializers.ModelSerializer):
    """ A serializer for categories. """

    box_set = BoxChildSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Category
        fields = (
            "name",
            "slug",
            "order",
            "description",
            "box_set"
        )
