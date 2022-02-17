from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home1$', views.home1),
    url(r'^header$', views.header),
    url(r'^header1$', views.header1),
    url(r'^footer$', views.footer),
    url(r'^about$', views.about),
    url(r'^about1$', views.about1),
    url(r'^media$', views.media),
    url(r'^blog1$', views.blog1),
    url(r'^login$', views.login),
    url(r'^creg$', views.creg),
    url(r'^spologin$', views.spologin),
    url(r'^sreg$', views.sreg),
    url(r'^login1save$', views.login1save),
    url(r'^register1$', views.register1),
    url(r'^logout1$', views.logout1),
    url(r'^logout1new$', views.logout1new),
    url(r'^login2save$', views.login2save),
    url(r'^register2$', views.register2),
    url(r'^logout2$', views.logout2),
    url(r'^logout2new$', views.logout2new),
    url(r'^contactsave$', views.contactsave),
    url(r'^predonation$', views.predonation),
    url(r'^show2new$', views.show2new),
    url(r'^shownew$', views.shownew),
    url(r'^report$', views.report),
    url(r'^report1$', views.report1),
    url(r'^show$', views.show),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^deletenew/(?P<id>\d+)$', views.deletenew),
    url(r'^save1$', views.save1),
    url(r'^show1$', views.show1),
    url(r'^delete1/(?P<Pre_id>\d+)$', views.delete1),
    url(r'^delete1new/(?P<Pre_id>\d+)$', views.delete1new),


]
