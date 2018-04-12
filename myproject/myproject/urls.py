from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','cache.views.home'), #me lleva a la pagina PRINCIPAL
    url(r'^(\S+)$','cache.views.pagina'),
)
