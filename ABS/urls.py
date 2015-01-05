from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ABS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "homepage.views.homeview", name="home_page_view"),

    url(r"^contact/$", "homepage.views.email_compose", name="home_page_view"),
    # url(r"^test/$", "homepage.views.test", name="home_page_view"),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))