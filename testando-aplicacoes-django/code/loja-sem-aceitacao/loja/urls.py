from django.conf.urls import include, patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from loja.vitrine import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contato$', views.Contato.as_view(), name='contato'),
)
