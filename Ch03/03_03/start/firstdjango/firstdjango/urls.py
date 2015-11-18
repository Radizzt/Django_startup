from django.conf.urls import include, url
from django.contrib import admin
from inventory import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r"^item/(?P<id>\d+)/", views.item_detail, name="item_detail"),#(?P) = name group, will be use as a parameter
    url(r'^admin/', include(admin.site.urls)),
]
