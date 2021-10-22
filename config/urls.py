""" Main URLs Module. """

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include(('bigbox.core.urls', 'core'), namespace='core')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
