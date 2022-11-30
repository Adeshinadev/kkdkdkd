# Class which handles all entry point url patterns.
from django.conf.urls import include, url
from django.contrib import admin

# Set admin to auto discover.
admin.autodiscover()
from django.urls import path, include

# Url patterns, I.e. all url's for the application.

urlpatterns = [
    # Pattern for the admin directory.
    path('admin/', admin.site.urls),
    path('', include('health.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # # Pattern for the root directory, I.e. this will load the actual applications url's.
    # url(r'^', include('health.urls', namespace='health'))
]
