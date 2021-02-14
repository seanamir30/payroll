from django.conf.urls import url
from . import views

#This code is for creating new pages and redirecting to their URLS.

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^employee/$', views.next_employee, name='next_employee'),
    url(r'^employer/$', views.next_employer, name='next_employer'),
    url(r'^add_employee_form_submit/$', views.add_employee_form_submit, name='add_employee_form_submit'),
    url(r'^search_employee_form_submit/$', views.search_employee_form_submit, name='search_employee_form_submit'),

]