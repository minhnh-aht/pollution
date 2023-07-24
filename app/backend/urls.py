from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django cms urls
    path('admin/', admin.site.urls),
    path("", include("djangocms_page_sitemap.sitemap_urls")),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path("select2/", include("django_select2.urls")),

    # Pollution custom urls

]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns.append(path('', include('cms.urls')))

# the new django admin sidebar is bad UX in django CMS custom admin views.
admin.site.enable_nav_sidebar = False
