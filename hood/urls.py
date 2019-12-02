from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
        url('^$', views.index, name = 'index'),
        url(r'^home$', views.home, name = 'home'),
        url(r'^accounts/profile/$', views.profile, name = 'profile'),
        url(r'^services$', views.services, name = 'services'),
        url(r'^business$', views.business, name = 'business'),
        url(r'^about$', views.about, name = 'about'),
        url(r'^user_admin$', views.user_admin, name = 'user_admin'),
        url(r'^category$', views.category, name = 'category'),
        url(r'^newneighbourhood$', views.newneighbourhood, name = 'newneighbourhood'),
        url(r'^newservice$', views.newservice, name = 'newservice'),
        url(r'^newbusiness$', views.newbusiness, name = 'newbusiness'),
        url(r'^search$', views.search, name = 'search'),
        url(r'^change$', views.change, name = 'change'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)