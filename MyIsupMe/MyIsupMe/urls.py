from django.conf.urls import patterns, include, url
import MyIsupMe.views as vista

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyIsupMe.views.home', name='home'),
    # url(r'^MyIsupMe/', include('MyIsupMe.foo.urls')),
    url(r'^$', vista.home),
    url(r'^verificacion$', vista.verificacionredirect),
    url(r'^verificacion/(\S+)$', vista.verificacion),
    url(r'^\S+$', vista.errores),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
