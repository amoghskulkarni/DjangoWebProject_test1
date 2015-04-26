"""
Definition of urls for DjangoWebProject_test1.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login$', 'app.views.login', name='login'),
    url(r'^logout$', 'app.views.logout', name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^mypage$', 'app.views.mypage', name='mypage'),
    url(r'^upload$', 'app.views.uploadFile', name='uploadFile'),
    url(r'^testPost$', 'app.views.testPost', name='testPost'),
    url(r'^applyAnalysis$', 'app.views.applyAnalysis', name='applyAnalysis'),
    url(r'^register$', 'app.views.register', name='register'),
    url(r'^register_success$', 'app.views.register_success', name='register_success'),
    url(r'^suggestions$', 'app.views.suggestions', name='suggestions'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
