from django.conf.urls import patterns, include, url

urlpatterns = patterns('www.views',
    url(r'^$', 'home.index', name='www.home'),
    url(r'^about/$', 'home.about', name='www.about'),
    url(r'^adjutor/$', 'home.adjutor', name='www.adjutor'),
    url(r'^contact/$', 'home.contact', name='www.contact'),
    url(r'^portfolio/$', 'home.portfolio', name='www.portfolio'),
)

