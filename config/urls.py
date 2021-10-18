""" Main URLs Module. """

from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
]
