""" Main URLs Module. """

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include(('bigbox.core.urls', 'core'), namespace='core')),
]
