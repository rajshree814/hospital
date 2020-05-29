from django.conf.urls import url
from basic_app import views
from basic_app.views import SignUpView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'basic_app'
urlpatterns = [
    url(r'^$', views.index.as_view(),name = 'index'),
    url(r'createp/',views.createp.as_view(),name ='createp'),
    url(r'patient_list/$',views.listp.as_view(),name = 'patient_list'),
    url(r'updatep/(?P<pk>\d+)/$',views.updatep.as_view(),name = 'updatep'),
    url(r'updateh/(?P<pk>\d+)/$',views.updateh.as_view(),name = 'updateh'),
    url(r'updated/(?P<pk>\d+)/$',views.updated.as_view(),name = 'updated'),
    url(r'details/(?P<pk>\d+)/$',views.details.as_view(),name ='details'),
    url(r'createh/',views.createh.as_view(),name ='createh'),
    url(r'hospital_details/(?P<pk>\d+)/$',views.hospital_details.as_view(),name ='hospital_details'),
    url(r'hospital_list/$',views.listh.as_view(),name = 'hospital_list'),
    url(r'patient_list/(?P<pk>\d+)/$',views.details.as_view(),name = 'patient_list'),
    url(r'hospital_list/(?P<pk>\d+)/$',views.hospital_details.as_view(),name = 'hospital_list'),
    url(r'patient_confirm_delete/(?P<pk>\d+)/$',views.deletep.as_view(),name = 'patient_confirm_delete'),
    url(r'hospital_confirm_delete/(?P<pk>\d+)/$',views.deleteh.as_view(),name = 'hospital_confirm_delete'),
    url(r'doctors_confirm_delete/(?P<pk>\d+)/$',views.deleted.as_view(),name = 'doctors_confirm_delete'),
    url('basic_app_pivot',views.basic_app_pivot,name ='basic_app_pivot'),
    url('data',views.pivot_data,name ='pivot_data'),
    url(r'created/',views.created.as_view(),name ='created'),
    url(r'doctors_list/$',views.doctors_list.as_view(),name = 'doctors_list'),
    url(r'doctors_list/(?P<pk>\d+)/$',views.details.as_view(),name = 'doctors_list'),
    url(r'signup/',views.SignUpView.as_view(),name='signup'),
    url(r'login/',views.loginview.as_view(),name='login'),
    url(r'logout/',views.logoutview.as_view(),name='logout'),
]
