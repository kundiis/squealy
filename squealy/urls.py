from django.conf.urls import url
from django.contrib.auth.decorators import login_required

import views

urlpatterns = [
   url(r'charts/$', login_required(views.ChartsLoaderView.as_view())),
   url(r'user/$', login_required(views.UserInformation.as_view())),
   url(r'squealy/(?P<chart_url>[-\w]+)', login_required(views.ChartView.as_view())),
   url(r'databases/$', login_required(views.DatabaseView.as_view())),
   url(r'^send-email/(?P<chart_url>[-\w]+)/$', views.temp_report),
   url(r'^$', login_required(views.squealy_interface)),
   url(r'^(?P<chart_name>[\w@%.\Wd]+)/$', login_required(views.squealy_interface)),
   url(r'^(?P<chart_name>[\w@%.\Wd]+)/(?P<mode>\w+)$', login_required(views.squealy_interface)),
]
