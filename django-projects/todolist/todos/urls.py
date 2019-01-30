from django.conf.urls import url


from . import views

urlpatterns=[
	url(r'details/(?P<id>\w{0,50})/$',views.details,name="detail"),
	url(r'add/$',views.add,name="add"),
	url(r'^$', views.index,name="index")
]