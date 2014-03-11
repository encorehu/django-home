from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import RootTextView, HomeView

urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(),
        name='home'),

    (r'^(?i)favicon.ico$',     'django.views.static.serve', {'path':'favicon.ico','document_root' : settings.STATIC_ROOT}),

    url(r'^(?P<filename>.*).txt$',
        RootTextView.as_view()
        ),
)
