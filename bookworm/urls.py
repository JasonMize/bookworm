from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookcases/', include('bookcases.urls', namespace='bookcases')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('core.urls', namespace='core'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)