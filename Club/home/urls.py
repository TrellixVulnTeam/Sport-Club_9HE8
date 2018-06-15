from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^all-trainings/$', views.display_trainings),
    url(r'^training-detail/(?P<training_id>\d+)/$', views.display_training),
    url(r'^training-detail/(?P<training_id>\d+)/update/$', views.update_training),
    url(r'^calendar/$', views.display_calendar),
    url(r'^profile/$', views.display_profile),
    url(r'^profile/update/$', views.update_profile),
]